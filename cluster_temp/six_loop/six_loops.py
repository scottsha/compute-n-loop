from sage.all_cmdline import *
import os, sys
from snappy import *

attach('/nv/hp24/esabo3/scratch/six_loop/nz_exact.py')
load('/nv/hp24/esabo3/scratch/six_loop/nz_exact.py')
diag_path = sys.argv[2]
all_diagrams = load(diag_path)

nz_data_file = sys.argv[1]
nz = load(nz_data_file)
E6 = nloop(nz, 6, all_diagrams)
invar = E6.nloop_invariant()
#result_data_file_path = os.path.join('results/', nz_data_file[16:-5] + '_invariants')
result_data_file_path = '/nv/hp24/esabo3/scratch/six_loop/results/6_loops/' + nz_data_file[49:-5] + '/' +nz_data_file[49:-5] + '_' + diag_path[59:]
#result = load(result_data_file_path)
#result[0] = result[0] + [invar]
save(invar, result_data_file_path)
