from __future__ import print_function
from sage.all import *

def matrix_texter(M):
    restrung=''
    b=''
    for a in str(M):
        if a=='[':
            restrung+='{'
        elif a==' ' and ( b==' ' or b=='[' or b==']'):
            restrung+=''
        elif a==' ':
            restrung+=','
        elif a==']':
            restrung+='}'            
        elif a=='\n':
            restrung+=','
        else:
            restrung+=a
        b=a
    restrung='{'+restrung
    restrung=restrung+'}'
    return restrung                        

def vector_texter(M):
    restrung=''
    b=''
    for a in str(M):
        if a=='(':
            restrung+='{'
        elif a==')':
            restrung+='}'            
        else:
            restrung+=a
        b=a
    return restrung                        

k_max=9
m_max=200
indix=[(k,m) for k in range(k_max+1) for m in range(m_max+1)]
for k,m in indix:
    try:
        name = 'K%d_%d' %(k,m)
        nz = load('../results/' + name + '_invariants.sobj')
        numfield = nz[1][5]
        embedding=nz[1][7]
        shapes = nz[1][6]
        A = matrix_texter(nz[1][0])
        B = matrix_texter(nz[1][1])
        nu = nz[1][2]
        nu = vector_texter(nu)
        f = nz[1][3]
        f = vector_texter(f)
        fp = nz[1][4]
        fp = vector_texter(fp)
        textfile = open('../results/Text/' + name + '.txt','w')
        print('# Manifold '+name, file=textfile)
        print(file=textfile)    
        print('# Number Field', file=textfile)
        print('%s \n' %str(numfield), file=textfile)
        print('# Approximate Field Generator', file=textfile)
        print(embedding, file=textfile)
        print(file=textfile)
        print('# Shape Parameters', file=textfile)
        for shape in shapes:
            print('%s' %str(shape), file=textfile)
            print(file=textfile)
        print(file=textfile)
        print('# A Gluing Matrix', file=textfile)
        print(A, file=textfile)
        print(file=textfile)
        print('# B Gluing Matrix', file=textfile)
        print(B, file=textfile)
        print(file=textfile)
        print('# nu Gluing Vector', file=textfile)
        print(nu, file=textfile)
        print(file=textfile)
        print('# f Combinatorial flattening', file=textfile)
        print(f, file=textfile)
        print(file=textfile)
        print('# f\' Combinatorial flattening', file=textfile)
        print(fp, file=textfile)
        print(file=textfile)
        for i, invar in enumerate(nz[0]):
            print('# %d Loop Invariant' %(i+1), file=textfile)
            print(invar, file=textfile)
            print(file=textfile)
        textfile.close()
    except:
        pass
