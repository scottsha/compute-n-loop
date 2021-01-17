from sage.all_cmdline import *

#K2
for m in range(1,2):
    name = 'K2_%d' %m

    nz = load('../results/' + name + '_invariants.sobj')
    numfield = nz[1][5]
    shapes = nz[1][6]
    A = nz[1][0]
    B = nz[1][1]
    nu = nz[1][2]
    f = nz[1][3]
    fp = nz[1][4]
    oneloop = nz[0][0]
    twoloop = nz[0][1]
    threeloop = nz[0][2]
    fourloop = nz[0][3]
    fiveloop = nz[0][4]

    textfile = open('../results/Text/' + name + '.txt','w')
    print('#Manifold'+name, file=textfile)    
    print('#Number Field', file=textfile)
    print('%s \n' %str(numfield), file=textfile)
    print('#Shape Parameters', file=textfile)
    for shape in shapes:
        print('%s' %str(shape), file=textfile)
    print(file=textfile)
    print('#A Gluing Matrix', file=textfile)
    print(A, file=textfile)
    print(file=textfile)
    print('#B Gluing Matrix', file=textfile)
    print(B, file=textfile)
    print(file=textfile)
    print('#nu Gluing Vector', file=textfile)
    print(nu.column(), file=textfile)
    print(file=textfile)
    print('#f Combinatorial flattening', file=textfile)
    print(nu.column(), file=textfile)
    print(file=textfile)
    print('#f\' Combinatorial flattening', file=textfile)
    print(nu.column(), file=textfile)
    print(file=textfile)
    print('#One Loop Invariant', file=textfile)
    print(oneloop, file=textfile)
    print(file=textfile)
    print('#Two Loop Invariant', file=textfile)
    print(twoloop, file=textfile)
    print(file=textfile)
    print('#Three Loop Invariant', file=textfile)
    print(threeloop, file=textfile)
    print(file=textfile)
    print('#Four Loop Invariant', file=textfile)
    print(fourloop, file=textfile)
    print(file=textfile)
    print('#Five Loop Invariant', file=textfile)
    print(fiveloop, file=textfile)
    textfile.close()

#K3
for m in range(1,3):
    name = 'K3_%d' %m

    nz = load('../results/' + name + '_invariants.sobj')
    numfield = nz[1][5]
    shapes = nz[1][6]
    A = nz[1][0]
    B = nz[1][1]
    nu = nz[1][2]
    f = nz[1][3]
    fp = nz[1][4]
    oneloop = nz[0][0]
    twoloop = nz[0][1]
    threeloop = nz[0][2]
    fourloop = nz[0][3]
    fiveloop = nz[0][4]

    textfile = open('../results/Text/' + name + '.txt','w')
    #Write the textfile here using however formatting you wish
    #Note that nu, f, and fp should be transposed. idk how you want to handle that. I'd just ignore it?
    #Also note that shapes is a list and you might wish to print them all out one by one. there is one shape per tetra. so any loop will have to be that long
    textfile.close()

#K4
for m in range(1,5):
    name = 'K4_%d' %m

    nz = load('../results/' + name + '_invariants.sobj')
    numfield = nz[1][5]
    shapes = nz[1][6]
    A = nz[1][0]
    B = nz[1][1]
    nu = nz[1][2]
    f = nz[1][3]
    fp = nz[1][4]
    oneloop = nz[0][0]
    twoloop = nz[0][1]
    threeloop = nz[0][2]
    fourloop = nz[0][3]
    fiveloop = nz[0][4]

    textfile = open('../results/Text/' + name + '.txt','w')
    #Write the textfile here using however formatting you wish
    #Note that nu, f, and fp should be transposed. idk how you want to handle that. I'd just ignore it?
    #Also note that shapes is a list and you might wish to print them all out one by one. there is one shape per tetra. so any loop will have to be that long
    textfile.close()

#K5
for m in range(1,23):
    name = 'K5_%d' %m

    nz = load('../results/' + name + '_invariants.sobj')
    numfield = nz[1][5]
    shapes = nz[1][6]
    A = nz[1][0]
    B = nz[1][1]
    nu = nz[1][2]
    f = nz[1][3]
    fp = nz[1][4]
    oneloop = nz[0][0]
    twoloop = nz[0][1]
    threeloop = nz[0][2]
    fourloop = nz[0][3]
    fiveloop = nz[0][4]

    textfile = open('../results/Text/' + name + '.txt','w')
    #Write the textfile here using however formatting you wish
    #Note that nu, f, and fp should be transposed. idk how you want to handle that. I'd just ignore it?
    #Also note that shapes is a list and you might wish to print them all out one by one. there is one shape per tetra. so any loop will have to be that long
    textfile.close()

#K6
for m in range(1,44):
    name = 'K7_%d' %m

    nz = load('../results/' + name + '_invariants.sobj')
    numfield = nz[1][5]
    shapes = nz[1][6]
    A = nz[1][0]
    B = nz[1][1]
    nu = nz[1][2]
    f = nz[1][3]
    fp = nz[1][4]
    oneloop = nz[0][0]
    twoloop = nz[0][1]
    threeloop = nz[0][2]

    textfile = open('../results/Text/' + name + '.txt','w')
    #Write the textfile here using however formatting you wish
    #Note that nu, f, and fp should be transposed. idk how you want to handle that. I'd just ignore it?
    #Also note that shapes is a list and you might wish to print them all out one by one. there is one shape per tetra. so any loop will have to be that long
    textfile.close()

#K7
for m in range(1,130):
    name = 'K7_%d' %m

    nz = load('../results/' + name + '_invariants.sobj')
    numfield = nz[1][5]
    shapes = nz[1][6]
    A = nz[1][0]
    B = nz[1][1]
    nu = nz[1][2]
    f = nz[1][3]
    fp = nz[1][4]
    oneloop = nz[0][0]
    twoloop = nz[0][1]
    threeloop = nz[0][2]

    textfile = open('../results/Text/' + name + '.txt','w')
    #Write the textfile here using however formatting you wish
    #Note that nu, f, and fp should be transposed. idk how you want to handle that. I'd just ignore it?
    #Also note that shapes is a list and you might wish to print them all out one by one. there is one shape per tetra. so any loop will have to be that long
    textfile.close()
