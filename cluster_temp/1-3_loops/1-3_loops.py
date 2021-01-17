from sage.all_cmdline import *
import os, sys
from snappy import *
import time

attach('/nv/hp24/esabo3/scratch/1-3_loops/nz_exact.py')
load('/nv/hp24/esabo3/scratch/1-3_loops/nz_exact.py')

nz_data_file = sys.argv[1]
nz = load(nz_data_file)

#2-loop
t0 = time.time()
two_diags = load('/nv/hp24/esabo3/scratch/1-3_loops/data_precomputed_diagrams/2diagrams.sobj')
E = nloop(nz, 2, two_diags)
invar2 = E.nloop_invariant()
t1 = time.time()
print '2-loop: ' + str(t1 - t0) + ' seconds'

#1-loop
t0 = time.time()
E = nloop(nz, 1, two_diags)
invar1 = E.one_loop()
t1 = time.time()
print '1-loop: ' + str(t1 - t0) + ' seconds'

#3-loop
t0 = time.time()
three_diags = load('/nv/hp24/esabo3/scratch/1-3_loops/data_precomputed_diagrams/3diagrams.sobj')
E = nloop(nz, 3, three_diags)
invar3 = E.nloop_invariant()
t1 = time.time()
print '3-loop: ' + str(t1 - t0) + ' seconds'

#4-loop
t0 = time.time()
four_diags = load('/nv/hp24/esabo3/scratch/1-3_loops/data_precomputed_diagrams/4diagrams.sobj')
E = nloop(nz, 4, four_diags)
invar4 = E.nloop_invariant()
t1 = time.time()
print '4-loop: ' + str(t1 - t0) + ' seconds'

directory = '/nv/hp24/esabo3/scratch/1-3_loops/results/' #+ nz_data_file[49:-5]
#if not os.path.exists(directory):
#    os.makedirs(directory)
result_data_file_path = directory + '/' + nz_data_file[49:-5] + '_invariants.sobj'
save([[invar1, invar2, invar3, invar4], nz], result_data_file_path)
