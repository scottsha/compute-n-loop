import os
from sage.all_cmdline import *

for folder in os.listdir('results/6_loops'):
    #if folder != '.DS_Store':
    if folder == 'K4_1':
        invar = 0
        vf = 0
        count = 0
        for result_temp_file in os.listdir('results/6_loops/' + folder):
            if result_temp_file != '.DS_Store':
                temp_invar = load('results/6_loops/' + folder + '/' + result_temp_file)
                invar = invar + temp_invar[0]
                if count == 0:
                    invar = invar + temp_invar[1]
                    count = 1

        result = load('results/' + folder + '_invariants.sobj')
        result[0] = result[0] + [invar]
        save(result, 'results/' + folder + '_invariants.sobj')
        print invar
        print 'Completed: ' + folder
