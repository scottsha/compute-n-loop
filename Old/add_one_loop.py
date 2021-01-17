import os

for nz_data_file in os.listdir('nzdata'):
    if nz_data_file != '.DS_Store':
        if os.path.exists('results/' + nz_data_file[9:-5] + '_invariants.sobj'):
            nz_data_file_path = os.path.join('nzdata', nz_data_file)
            nz = load(nz_data_file_path)
            E = nloop(nz, 1, all_diagrams)
            invar = E.one_loop()
            result_data_file_path = os.path.join('results', nz_data_file[9:-5] + '_invariants')
            result = load(result_data_file_path)
            result[0] = [invar] + result[0]
            save(result, result_data_file_path)
            print 'Completed: ' + result_data_file_path


