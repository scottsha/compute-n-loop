# -*- coding: utf-8 -*-

from sequence_generator import SeqGen
from sage.all_cmdline import *

diag = load('../data_precomputed_diagrams/6diagrams.sobj')
len_split = 50.
len_list = ceil(len(diag)/len_split)
list = [None]*len_list

count = 0
for i in SeqGen(4, 'abcdefghijklmnopqrstuvwxyz'):
    if count < len_list:
        list[count] = i.rjust(4, 'a')
    count = count + 1
save(list,'split_file_list.sobj')

file = open('split6_sage_code.py','w')
file.write("from sage.all_cmdline import *\n")
file.write("diag = load('../data_precomputed_diagrams/6diagrams.sobj')\n")
for i in range(len_list):
    file.write("temp = diag[%d:%d]; save(temp, '../data_precomputed_diagrams/6_split_small/6%s.sobj')\n" %((i*len_split),((i+1)*len_split), str(list[i])))
file.close()
