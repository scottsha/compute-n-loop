from snappy import *
import sage

attach('nz_exact_all.py')
load('nz_exact_all.py')
all_diagrams = load('data_precomputed_diagrams/6diagrams.sobj')
for m in range(1,23):
    nz = load('nzdata/nz_exact_K5_%d.sobj' %m)
    E2 = nloop(nz, 2, all_diagrams)
    E3 = nloop(nz, 3, all_diagrams)
    E4 = nloop(nz, 4, all_diagrams)
    E5 = nloop(nz, 5, all_diagrams)
    e2 = E2.nloop_invariant()
    e3 = E3.nloop_invariant()
    e4 = E4.nloop_invariant()
    e5 = E5.nloop_invariant()
    result=[[e2,e3,e4,e5],nz]
    save(result, 'nloop_data/K5_%d_invariants.sobj' %m)


