from snappy import *
import sage

attach('nz_exact_all.py')
load('nz_exact_all.py')

all_diagrams = load('data_precomputed_diagrams/6diagrams.sobj')
manifold_list = [M.name() for M in CensusKnots if M.num_tetrahedra() <= 5]
n_list = [2, 3, 4]

results = [[[M, n, nloop_automated(Manifold(M), n, all_diagrams)]\
    for n in n_list] for M in manifold_list]

save(results, 'results.sobj')

