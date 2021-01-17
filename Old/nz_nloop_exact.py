#import os, sys, re, snappy, hypertorsion
import random as randmodule
import snappy.snap as snap
from sage.all import *

def all_shape_parameters(z):
    return [z, 1/(1-z), 1 - 1/z]

def in_threes(L):
    return [L[3*i : 3*(i+1)] for i in range(len(L)//3)]

def shift_in_threes(L, shifts):
    return sum( [ X[s:]+X[:s] for X, s in zip(in_threes(L), shifts)], [])

def every_third_elem(L, shift):
    return [L[i] for i in range(shift, len(L), 3)]

def epsilon(CC, d):
    return 2**(-CC.precision()//d)

def exponentiate_list(L, E):
    return prod([l**e for l, e in zip(L, E)])

pari.set_real_precision(100)

def is_geom(M,c):
    vol = M.volume()
    for v in c.volume_numerical():
        if abs(v-vol)<1e-10:
            return True
    return False

class NeumannZagierDatum():
    """
    Examples of usage:
    
    sage: M = snappy.Manifold('5_2')
    sage: D = NeumannZagierDatum(M)
    sage: D.manifold
    5_2(0,0)
    sage: D.make_B_nondegenerate()
    1
    sage: D.make_B_nondegenerate()
    0
    sage: D.make_B_nondegenerate()
    0
    sage: A, B, v = D.ABv_square()
    sage: f, fdd = D.f_and_fddot()
    sage: shapes = D.shapes(1000)
    sage: nz.exact_shapes_via_ptolemy()
    [Mod(-x, x^3 + 2*x^2 + 3*x + 1),
    Mod(x^2 + x + 2, x^3 + 2*x^2 + 3*x + 1),
    Mod(-x, x^3 + 2*x^2 + 3*x + 1)]
    sage: t = D.one_loop()
    sage: D.one_loop_exact() 
    sage: D.check()
    sage: D.check_exact()
    """
    def __init__(self, manifold, N=2):
        self.manifold = manifold

        self.N = N
        if N == 2:
            self._raw_gluing_equations = manifold.gluing_equations()
        else:
            self._raw_gluing_equations = manifold.gluing_equations_pgl(N).matrix

        self.num_shapes = n = self._raw_gluing_equations.ncols()//3
        self.num_eqns = self._raw_gluing_equations.nrows()
        self._eliminated_shapes = n*[1,]

    def shapes(self, precision=None, shapes=None):
        if shapes:
            base_shapes = shapes
        else:
            if precision == None:
                base_shapes = [CC(z) for z in self.manifold.tetrahedra_shapes(part='rect')]
            else:
                base_shapes = hypertorsion.snap.polished_tetrahedra_shapes(
                    self.manifold, precision)

        if self.N > 2:
            cols = self.manifold.gluing_equations_pgl(self.N).explain_columns
            col_data = [int(c.split('_')[-1]) for c in cols if c[:2] == 'z_']
            base_shapes = [base_shapes[i] for i in col_data]
            
        return [ all_shape_parameters(z)[(i - 1) % 3]
                 for z, i in zip(base_shapes, self._eliminated_shapes)]

    def log_shapes(self, precision=None):
        return [log(z) for z in self.shapes(precision)]

    def all_log_shapes(self, precision=None):
        return sum( [ [log(w) for w in all_shape_parameters(z)] for z in self.shapes(precision)], []) 

    def gluing_equations(self):
        eqns = self._raw_gluing_equations
        new_cols = shift_in_threes(eqns.columns(), [(i - 1)%3 for i in self._eliminated_shapes])
        return matrix(new_cols).transpose()

    def ABCbar(self):
        eqns, n = self.gluing_equations(), self.num_shapes
        return [eqns.matrix_from_columns(range(i, 3*n, 3)) for i in range(3)]

    def target_vector(self):
        """
        Answer times pi*i is right-hand side of
        gluing equations.
        """
        m, c = self.num_eqns, self.manifold.num_cusps()
        if self.N == 2:
            return vector( ZZ, [2 for i in range(m - 2*c)] + (2*c)*[0] )
        else:
            rows = self.manifold.gluing_equations_pgl(self.N).explain_rows
            def right_hand_side(name):
                if name == None:
                    return 0
                return 0 if re.match('meridian|longitude', name) else 2
            return vector( ZZ, [ right_hand_side(name) for name in rows])
        
    def ABv(self):
        A, B, C = self.ABCbar()
        one = vector(B.base_ring(), B.ncols()*[1])
        return A - B, C - B, self.target_vector() - B*one

    def ABv_square(self, rows_to_eliminate=None):
        A, B, v = self.ABv()
        M = block_matrix([[B, A, v.column()]])
        c = self.manifold.num_cusps()

        if self.N == 2:
            rows = range(M.nrows())[:-2*c]
            rows += [2*i + rows[-1] + 1 for i in range(c)]
        else:
            row_meanings = self.manifold.gluing_equations_pgl(self.N).explain_rows
            rows = [ i for i, name in enumerate(row_meanings) if name[:4] != 'long']
            
        M = M.matrix_from_rows(rows)
        M = M.hermite_form(include_zero_rows=False)
        n = A.ncols()
        return M.matrix_from_columns(range(n, 2*n)), M.matrix_from_columns(range(n)), M.columns()[-1]

    def f_and_fddot(self):
        A, B, v = self.ABv_square()
        n = A.ncols()
        M = block_matrix([[A, B]])
        S, U, V = M.smith_form()
        d = S.diagonal()
        f = V*vector(ZZ, [ x/y for x, y in zip(U*v, d) ] + n*[0])
        assert M*f == v
        return vector(f[:n]), vector(f[n:])

    def make_B_nondegenerate(self):
        count = 0
        while det(self.ABv_square()[1]) == 0:
            self._eliminated_shapes = [randmodule.randrange(3) for i in range(self.num_shapes)]
            count += 1
        return count

    def nahm_datum(self):
        A, B, nu = self.ABv_square()
        f, fdd = self.f_and_fddot()
        NahmA = identity_matrix(A.nrows())-B.inverse()*A
        NahmB = (-B.inverse()*nu+vector([1 for i in range(A.nrows())]))/2
        NahmC = A.nrows()/24-f*B.inverse()*A*fdd/8
        return NahmA, NahmB, NahmC

    def exact_shapes_via_ptolemy(self):
        p = self.manifold.ptolemy_variety(2,'all')
        s = p.compute_solutions(verbose=True).flatten(depth=2)
        sol = [ c for c in s if is_geom(self.manifold,c) ][int(0)]
        cr = sol.cross_ratios()
        shapes = [cr['z_0000_%d' % i] for i in range(self.num_shapes)]
        return [ all_shape_parameters(z)[(i - 1) % 3]
                 for z, i in zip(shapes, self._eliminated_shapes)]

    def exact_shapes_via_ptolemy_lifted(self):
        p = self.manifold.ptolemy_variety(2,'all')
        s = p.compute_solutions(verbose=True).flatten(depth=2)
        sol = [ c for c in s if is_geom(self.manifold,c) ][int(0)]
        cr = sol.cross_ratios()
        shapes = [cr['z_0000_%d' % i] for i in range(self.num_shapes)]
        rot_shapes = [ all_shape_parameters(z)[(i - 1) % 3] \
                 for z, i in zip(shapes, self._eliminated_shapes)]
        lifted_shapes = [gp.lift(s) for s in rot_shapes] 
        return [sol.number_field(), lifted_shapes]

    def one_loop(self, precision=None, shapes=None):
        A, B, v = self.ABv_square()
        f, fdd = self.f_and_fddot()
        shapes = self.shapes(precision, shapes)
        shapes_dd = [1 - 1/z for z in shapes]
        CC = shapes[0].parent()
        D1 = diagonal_matrix(shapes_dd)
        D2 = diagonal_matrix([1/z for z in shapes])
        return (1/CC(2)) * det(A*D1 + B*D2) * exponentiate_list(shapes, fdd) * exponentiate_list(shapes_dd, -f)

    def one_loop_exact(self):
        A, B, v = self.ABv_square()
        f, fdd = self.f_and_fddot()
        shapes = self.exact_shapes_via_ptolemy()
        shapes_dd = [1 - 1/z for z in shapes]
        D1 = gp.matdiagonal(shapes_dd)
        D2 = gp.matdiagonal([1/z for z in shapes])
        return (1/QQ(2)) * gp.matdet(A*D1 + B*D2) * exponentiate_list(shapes, fdd) * exponentiate_list(shapes_dd, -f)
            
    def check_exact(self):
        z = self.exact_shapes_via_ptolemy()
        z_ddot = [1-1/s for s in z]
        A, B, v = self.ABv_square()
        Alist = [exponentiate_list(z,r) for r in A.rows()]
        Blist = [exponentiate_list(z_ddot,r) for r in B.rows()]
        answer = [Alist[i]*Blist[i]-(-1)**v[i] for i in range(self.num_shapes)]
        assert answer==[0 for i in range(self.num_shapes)]

    def check(self):
        shapes = vector( self.all_log_shapes() )
        CC = shapes[0].parent()
        eqns = self.gluing_equations()
        pi_I = CC.pi()*CC.gen()
        error = eqns * shapes - pi_I *self.target_vector()
        assert error.norm(Infinity) < epsilon(CC, 2)

        A, B, v = self.ABv()
        z = vector(every_third_elem(shapes, 0))
        z_ddot = vector(every_third_elem(shapes, 2))
        error = A*z + B*z_ddot - pi_I * v
        assert error.norm(Infinity) < epsilon(CC, 2)

def prepare_exact_nz_for_nloop_sage(manifold, file_name):
    M = manifold   # file_name = 'nz52.sobj'
    nz = NeumannZagierDatum(M)
    nz.make_B_nondegenerate()
    A = nz.ABv_square()[0]
    B = nz.ABv_square()[1]
    nu = nz.ABv_square()[2]
    f = nz.f_and_fddot()[0]
    f_ddot = nz.f_and_fddot()[1]
    p, shapes = nz.exact_shapes_via_ptolemy_lifted()
    S = PolynomialRing(QQ,'x')
    K = NumberField(S(str(p)),'y')
    new_shapes = [K(str(s.lift()).replace('x','y')) for s in shapes]
    pol = K.polynomial()
    new_nz = (A, B, nu, f, f_ddot, pol, new_shapes)
    save(new_nz, file_name)
        

    
