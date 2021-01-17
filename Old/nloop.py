"""
Compute the n-loop invariant S_n.

Reference: ``The Quantum Content of the Gluing Equations'' by
Dimofte and Garoufalidis.
"""
import operator
attach('polylogs.py')


def feynman_loop_number(diagram):
    """
    Calculate the Feynman Loop Number of a Diagram.
    
    The Feynman Loop Number of a connected looped multigraph
    is the number of 1-vertices+2-vertices + the number of loops
    """
    if diagram.num_edges() == 0:
        return 0
    return diagram.degree().count(1) + diagram.degree().count(2) + \
        diagram.num_edges() - diagram.num_verts() + 1


def symmetry_factor(diag):
    """
    Calculate the symmetry factor of a diagram.
    
    This is equal to the order of the group of vertex
    permutations preserving edges times k! for each
    k-multiedge times 2^number of loops
    """
    symfactor = diag.automorphism_group().cardinality()
    #  can use reduce(operator.mul, .) here to remove for loops?
    for foo in diag.vertices():
        for bar in range(foo, diag.num_verts()):
            conecs = diag.adjacency_matrix()[foo][bar]
            symfactor = kronecker_delta(foo, bar) * symfactor * 2 ** conecs * \
                factorial(conecs) + (1-kronecker_delta(foo, bar)) * \
                symfactor * factorial(conecs)
    return QQ(1)/symfactor


def bernoulli_plus_half(m):
    """Return bernoulli number with convention B1=+1/2."""
    return bernoulli(m)*(-1)**m


def polylogarithm(n, z):
    """Give the nth polylogarithm evaluated at z."""
    CC = z.parent()
    _ = gp.set_precision(z.prec())
    if (n, z) in prev:
        return prev[(n, z)]
    if n <= 0 and n >= -19:
        tmp = CC(gp.subst(polylog_dict[-(n + 20)], z_poly, z))
        prev[(n, z)] = tmp
        if len(prev) > 1000:
            prev.popitem(last=False)
        return tmp
    return CC(gp.subst(gp(polylog(n, x)), x, z))


def gamma(eye, kay, ell, n, nz_data):
    """Return the gamma equation for vertex_factor_tensor."""
    (A, B, nu, f, _, zees) = nz_data
    CC = nz_data[5][0].parent()
    _ = gp.set_precision(nz_data[5][0].prec())
    f = Matrix(f).transpose()
    if kay == 0:
        return sum([polylogarithm(2 - n, 1/z) for z in zees]) * \
            bernoulli_plus_half(n)/factorial(n) + kronecker_delta(n, 2) * \
            (f.transpose() * B.inverse() * A * f/8)[0][0]
    return (-1)**kay * sum([h**(bar - 1)/factorial(bar) *
        bernoulli_plus_half(bar) * polylogarithm(2 - bar - kay,
        1/zees[eye]) for bar in range((kronecker_delta(kay, 1) +
        kronecker_delta(kay, 2)), 1 + (kronecker_delta(kay, 1) +
        kronecker_delta(kay, 2)) + n - ell)]) - \
        kronecker_delta(kay, 1) * CC(0.5) * (B.inverse()*nu)[eye]


def vertex_factor_tensor(nz_data, n):
    """
    Generate vertex gamma as a tensor access values.

    Output is in the form
    vertexGamma[feynman_loop_number][vertex_degree][ith_shape_parameter]
    """
    var('h')
    (_, _, _, _, _, zees) = nz_data
    return [[[gamma(eye, kay, ell, n, nz_data) for eye in
        range(len(zees))] for kay in range(2*n + 1)] for ell in
        range(n + 1)]


def diagram_contribution_to_nloop(nz_data, n, diagram, ver_factor):
    """Compute the diagram contribution to the n loop invariant."""
    var('h')
    (A, B, _, _, _, zees) = nz_data
    CC = nz_data[5][0].parent()
    _ = gp.set_precision(nz_data[5][0].prec())
    N = len(zees)
    hamil = -B.inverse()*A + diagonal_matrix([1/(1 - z) for z in zees])
    prop = h*hamil.inverse()
    temp_sum = CC(0)
    for foo in range(N**diagram.num_verts()):
        indices = [floor(foo/(N**bar)) % N for bar in
            range(diagram.num_verts())]
        temp_sum += reduce(operator.mul, [prop[indices[eee[0]]]
            [indices[eee[1]]] for eee in diagram.edges
            (labels=False)] +
            [ver_factor[feynman_loop_number(diagram)]
            [diagram.degree()[vee]][indices[vee]] for vee in
            diagram.vertices()], 1).expand()
    return symmetry_factor(diagram)*temp_sum.coeff(h, n - 1)


def nloop_invariant(nz_data, n, diagrams):
    """Calculate the Dimofte-Garoufalidis n-loop invariant."""
    CC = nz_data[5][0].parent()
    _ = gp.set_precision(nz_data[5][0].prec())
    pre_comp_vertex_factor = vertex_factor_tensor(nz_data, n)
    diagrams = [g for g in diagrams if feynman_loop_number(g) <= n]
    loop_invar = sum([diagram_contribution_to_nloop(nz_data,
        n, diag, pre_comp_vertex_factor) for diag in diagrams]) + \
        pre_comp_vertex_factor[n][0][0]
    return loop_invar
