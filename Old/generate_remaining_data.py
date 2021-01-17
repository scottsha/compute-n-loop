import os
from snappy import *
import sage *

attach('nz_exact_all.py')
load('nz_exact_all.py')
all_diagrams = load('data_precomputed_diagrams/6diagrams.sobj')

for nz_data_file in os.listdir('nzdata'):
    if nz_data_file != '.DS_Store':
        if os.path.exists('results/' + nz_data_file[9:-5] + '_invariants.sobj') == False:
            nz_data_file_path = os.path.join('nzdata', nz_data_file)
            nz = load(nz_data_file_path)
            E1 = nloop(nz, 1, all_diagrams)
            E2 = nloop(nz, 2, all_diagrams)
            E3 = nloop(nz, 3, all_diagrams)
            e1 = E1.one_loop()
            e2 = E2.nloop_invariant()
            e3 = E3.nloop_invariant()
            result = [[e1,e2,e3],nz]
            result_data_file_path = os.path.join('results', nz_data_file[9:-5] + '_invariants')
            save(result, result_data_file_path)
            print 'Completed: ' + result_data_file_path
