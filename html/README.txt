# NEUMANN-ZAGIER DATA

A Neumann-Zagier datum is a 6-tuple (A,B,nu,f,f'',z), where

* A,B are N by N matrices (N=number of tetrahedra of an ideal triangulation
of a 1-cusped manifold), 

* nu,f,f'' are column N-vectors, (f,f'') are flattenings and Af+B f''=nu

* z is an N-vector of shape parameters. These are elements of the 
invariant trace field, which is defined by the Number Field polynomial, 
and embedded in the complex numbers via the Selected Root.

Here (A|B) is the Neumann-Zagier matrix where we remove one edge equation 
and replace it with the meridian cusp equation, and in addition we remove 
the z'=1/(1-z) variable. Hence A is the exponent matrix of z and B is the 
exponent matrix of z''=1-1/z. In addition, we choose B such that its
determinant is nonzero.

The n-loop invariants of a Neumann-Zagier datum are defined in 
<a href="http://www.math.gatech.edu/~stavros/publications/quantum.content.pdf">The quantum content of the gluing equations </span></a>.

# USAGE

# COMPUTATION OF EXACT N-LOOP INVARIANTS FROM MANIFOLD

from snappy import *
attach('nloop_exact.py')
load('nloop_exact.py')
all_diagrams = load('6diagrams.sobj')
M = Manifold('6_2')
nloop_from_manifold(M, 2, all_diagrams, engine="retrieve")

other options for engine: "magma" if available

# COMPUTATION OF EXACT N-LOOP INVARIANTS FROM PRECOMPUTED NZ-DATA

from snappy import *
attach('nloop_exact.py')
load('nloop_exact.py')
all_diagrams = load('6diagrams.sobj')
nz62 = load('nzdata/nz_exact_K5_19.sobj')
nloop_from_nzdatum(nz62, 2, all_diagrams)

# MANUAL COMPUTATION OF EXACT N-LOOP INVARIANTS FROM MANIFOLD

from snappy import *
attach('nloop_exact.py')
load('nloop_exact.py')
all_diagrams = load('6diagrams.sobj')
M = Manifold('6_2')
D = NeumannZagierDatum(M, engine="retrieve")
D.generate_nz_data()
E = nloop(D.nz, 2, all_diagrams)
E.nloop_invariant()
E.one_loop()

# GENERATE EXACT NZ-DATA

from snappy import *
attach('nloop_exact.py')
M = Manifold('6_2')
D = NeumannZagierDatum(M, engine="retrieve")
D.generate_nz_data()
D.nz

