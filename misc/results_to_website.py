from sage.all_cmdline import *
import sys
import sage

nz = load('results/' + sys.argv[1] + '_invariants.sobj')
print latex(nz[1][5]) + '\n\n'
for i in range(len(nz[1][6])):
    print latex(nz[1][6][i]) + '\n\n'
print latex(nz[1][0]) + '\n\n'
print latex(nz[1][1]) + '\n\n'
print latex(nz[1][2]) + '^T\n\n'
print latex(nz[1][3]) + '^T\n\n'
print latex(nz[1][4]) + '^T\n\n'
print latex(nz[0][0]) + '\n\n'
print latex(nz[0][1]) + '\n\n'
print latex(nz[0][2]) + '\n\n'
