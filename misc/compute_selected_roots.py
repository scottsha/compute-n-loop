from snappy import *
from sage.all_cmdline import *
import os
attach('nloop_exact.py')
load('nloop_exact.py')

for nz_data_file in os.listdir('nzdata'):
    if nz_data_file != '.DS_Store' and nz_data_file[0] != '.':
	print nz_data_file
        nz = load('nzdata/' + nz_data_file)
        name = nz_data_file[9:-5]
        M = Manifold(name)
	try:
	    D = NeumannZagierDatum(M, engine="retrieve")
            root = D.compute_ptolemy_field_and_embedding()
	except:
            D = NeumannZagierDatum(M, engine="magma")
            root = D.compute_ptolemy_field_and_embedding()
        nz = nz + (root,)
        save(nz, 'nzdata/' + nz_data_file)
        if os.path.exists('results/' + name + '_invariants.sobj') == True:
            result = load('results/' + name + '_invariants.sobj')
            result[1] = nz
            save(result, 'results/' + name + '_invariants.sobj')
