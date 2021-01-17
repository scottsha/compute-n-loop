from snappy import *
from sage.all_cmdline import *

rootsfile = open('/Users/2kak7/Dropbox/compute-nloop/misc/roots.txt','r')
rootslist = rootsfile.readlines()
index = 0

#K2
for m in range(1,2):
    M = Manifold('K2_%d' %m)
    first = 'K2_{%d}' %m
    firstprime = 'K2_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
        if second[1] == '_':
            secondp = second[0:2] + '{' + second[2:len(second)] + '}'
            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">%s</span></a>' %(second, secondp)
        elif second[2] == '_':
            secondp = second[0:3] + '{' + second[3:len(second)] + '}'
            if int(second[0:2]) <= 10:
                second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">%s</span></a>' %(second, secondp)
            else:
                second = secondp
    else:
        second = '-'
    third = str(HTLinkExteriors.identify(M))
    if third != 'False':
        third = third[0:-5]
    else:
        third = '-'
    fourth = str(OrientableCuspedCensus.identify(M))
    if fourth != 'False':
        fourth = fourth[0:-5]
    else:
        fourth = '-'
    allnames = first+', ' +secondp+', '+third+', '+fourth

    nz = load('results/' + firstprime + '_invariants.sobj')
    numfield = str(nz[1][5])
    shapes = nz[1][6]
    A = str(nz[1][0])
    B = str(nz[1][1])
    nu = str(nz[1][2]) + '^T'
    f = str(nz[1][3]) + '^T'
    fp = str(nz[1][4]) + '^T'
    oneloop = str(nz[0][0])
    twoloop = str(nz[0][1])
    threeloop = str(nz[0][2])
    fourloop = str(nz[0][3])
    fiveloop = str(nz[0][4])

    template = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/Knot_Data_Template2.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("allnames",allnames)
    newdata = newdata.replace("secondname",second)
    newdata = newdata.replace("thirdname",third)
    newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(shapes[0]))
    newdata = newdata.replace("shape2",str(shapes[1]))
    newdata = newdata.replace("selroot",str(rootslist[index])[0:-3] + str(rootslist[index])[-2:len(rootslist[index])])
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)
    newdata = newdata.replace("fiveloop",fiveloop)

    htmlout = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/K2/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

    index = index + 1

#K3
for m in range(1,3):
    M = Manifold('K3_%d' %m)
    first = 'K3_{%d}' %m
    firstprime = 'K3_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
        if second[1] == '_':
            secondp = second[0:2] + '{' + second[2:len(second)] + '}'
            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
        elif second[2] == '_':
            secondp = second[0:3] + '{' + second[3:len(second)] + '}'
            if int(second[0:2]) <= 10:
                second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
            else:
                second = '' + secondp + ''
    else:
        second = '-'
    third = str(HTLinkExteriors.identify(M))
    if third != 'False':
        third = third[0:-5]
    else:
        third = '-'
    fourth = str(OrientableCuspedCensus.identify(M))
    if fourth != 'False':
        fourth = fourth[0:-5]
    else:
        fourth = '-'
    allnames = first+', ' +secondp+', '+third+', '+fourth

    nz = load('results/' + firstprime + '_invariants.sobj')
    numfield = str(nz[1][5])
    shapes = nz[1][6]
    A = str(nz[1][0])
    B = str(nz[1][1])
    nu = str(nz[1][2]) + '^T'
    f = str(nz[1][3]) + '^T'
    fp = str(nz[1][4]) + '^T'
    oneloop = str(nz[0][0])
    twoloop = str(nz[0][1])
    threeloop = str(nz[0][2])
    fourloop = str(nz[0][3])
    fiveloop = str(nz[0][4])

    template = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/Knot_Data_Template3.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("allnames",allnames)
    newdata = newdata.replace("secondname",second)
    newdata = newdata.replace("thirdname",third)
    newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(shapes[0]))
    newdata = newdata.replace("shape2",str(shapes[1]))
    newdata = newdata.replace("shape3",str(shapes[2]))
    newdata = newdata.replace("selroot",str(rootslist[index])[0:-3] + str(rootslist[index])[-2:len(rootslist[index])])
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)
    newdata = newdata.replace("fiveloop",fiveloop)

    htmlout = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/K3/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

    index = index + 1

#K4
for m in range(1,5):
    M = Manifold('K4_%d' %m)
    first = 'K4_{%d}' %m
    firstprime = 'K4_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
        if second[1] == '_':
            secondp = second[0:2] + '{' + second[2:len(second)] + '}'
            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
        elif second[2] == '_':
            secondp = second[0:3] + '{' + second[3:len(second)] + '}'
            if int(second[0:2]) <= 10:
                second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
            else:
                second = '' + secondp + ''
    else:
        second = '-'
    third = str(HTLinkExteriors.identify(M))
    if third != 'False':
        third = third[0:-5]
    else:
        third = '-'
    fourth = str(OrientableCuspedCensus.identify(M))
    if fourth != 'False':
        fourth = fourth[0:-5]
    else:
        fourth = '-'
    allnames = first+', ' +secondp+', '+third+', '+fourth

    nz = load('results/' + firstprime + '_invariants.sobj')
    numfield = str(nz[1][5])
    shapes = nz[1][6]
    A = str(nz[1][0])
    B = str(nz[1][1])
    nu = str(nz[1][2]) + '^T'
    f = str(nz[1][3]) + '^T'
    fp = str(nz[1][4]) + '^T'
    oneloop = str(nz[0][0])
    twoloop = str(nz[0][1])
    threeloop = str(nz[0][2])
    fourloop = str(nz[0][3])
    fiveloop = str(nz[0][4])

    template = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/Knot_Data_Template4.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("allnames",allnames)
    newdata = newdata.replace("secondname",second)
    newdata = newdata.replace("thirdname",third)
    newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(shapes[0]))
    newdata = newdata.replace("shape2",str(shapes[1]))
    newdata = newdata.replace("shape3",str(shapes[2]))
    newdata = newdata.replace("shape4",str(shapes[3]))
    newdata = newdata.replace("selroot",str(rootslist[index])[0:-3] + str(rootslist[index])[-2:len(rootslist[index])])
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)
    newdata = newdata.replace("fiveloop",fiveloop)

    htmlout = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/K4/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

    index = index + 1

#K5
for m in range(1,23):
    M = Manifold('K5_%d' %m)
    first = 'K5_{%d}' %m
    firstprime = 'K5_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
        if second[1] == '_':
            secondp = second[0:2] + '{' + second[2:len(second)] + '}'
            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
        elif second[2] == '_':
            secondp = second[0:3] + '{' + second[3:len(second)] + '}'
            if int(second[0:2]) <= 10:
                second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
            else:
                second = '' + secondp + ''
    else:
        second = '-'
    third = str(HTLinkExteriors.identify(M))
    if third != 'False':
        third = third[0:-5]
    else:
        third = '-'
    fourth = str(OrientableCuspedCensus.identify(M))
    if fourth != 'False':
        fourth = fourth[0:-5]
    else:
        fourth = '-'
    allnames = first+', ' +secondp+', '+third+', '+fourth

    nz = load('results/' + firstprime + '_invariants.sobj')
    numfield = str(nz[1][5])
    shapes = nz[1][6]
    A = str(nz[1][0])
    B = str(nz[1][1])
    nu = str(nz[1][2]) + '^T'
    f = str(nz[1][3]) + '^T'
    fp = str(nz[1][4]) + '^T'
    oneloop = str(nz[0][0])
    twoloop = str(nz[0][1])
    threeloop = str(nz[0][2])
    fourloop = str(nz[0][3])
    fiveloop = str(nz[0][4])

    template = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/Knot_Data_Template5.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("allnames",allnames)
    newdata = newdata.replace("secondname",second)
    newdata = newdata.replace("thirdname",third)
    newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(shapes[0]))
    newdata = newdata.replace("shape2",str(shapes[1]))
    newdata = newdata.replace("shape3",str(shapes[2]))
    newdata = newdata.replace("shape4",str(shapes[3]))
    newdata = newdata.replace("shape5",str(shapes[4]))
    newdata = newdata.replace("selroot",str(rootslist[index])[0:-3] + str(rootslist[index])[-2:len(rootslist[index])])
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)
    newdata = newdata.replace("fiveloop",fiveloop)

    htmlout = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/K5/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

    index = index + 1

#K6
for m in range(1,44):
    M = Manifold('K6_%d' %m)
    first = 'K6_{%d}' %m
    firstprime = 'K6_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
        if second[1] == '_':
            secondp = second[0:2] + '{' + second[2:len(second)] + '}'
            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
        elif second[2] == '_':
            secondp = second[0:3] + '{' + second[3:len(second)] + '}'
            if int(second[0:2]) <= 10:
                second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
            else:
                second = '' + secondp + ''
    else:
        second = '-'
    third = str(HTLinkExteriors.identify(M))
    if third != 'False':
        third = third[0:-5]
    else:
        third = '-'
    fourth = str(OrientableCuspedCensus.identify(M))
    if fourth != 'False':
        fourth = fourth[0:-5]
    else:
        fourth = '-'
    allnames = first+', ' +secondp+', '+third+', '+fourth

    nz = load('results/' + firstprime + '_invariants.sobj')
    numfield = str(nz[1][5])
    shapes = nz[1][6]
    A = str(nz[1][0])
    B = str(nz[1][1])
    nu = str(nz[1][2]) + '^T'
    f = str(nz[1][3]) + '^T'
    fp = str(nz[1][4]) + '^T'
    oneloop = str(nz[0][0])
    twoloop = str(nz[0][1])
    threeloop = str(nz[0][2])

    template = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/Knot_Data_Template6.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("allnames",allnames)
    newdata = newdata.replace("secondname",second)
    newdata = newdata.replace("thirdname",third)
    newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(shapes[0]))
    newdata = newdata.replace("shape2",str(shapes[1]))
    newdata = newdata.replace("shape3",str(shapes[2]))
    newdata = newdata.replace("shape4",str(shapes[3]))
    newdata = newdata.replace("shape5",str(shapes[4]))
    newdata = newdata.replace("shape6",str(shapes[5]))
    newdata = newdata.replace("selroot",str(rootslist[index])[0:-3] + str(rootslist[index])[-2:len(rootslist[index])])
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)

    htmlout = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/K6/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

    index = index + 1

#K7
for m in range(1,130):
    M = Manifold('K7_%d' %m)
    first = 'K7_{%d}' %m
    firstprime = 'K7_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
        if second[1] == '_':
            secondp = second[0:2] + '{' + second[2:len(second)] + '}'
            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
        elif second[2] == '_':
            secondp = second[0:3] + '{' + second[3:len(second)] + '}'
            if int(second[0:2]) <= 10:
                second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;"> %s </span></a>' %(second, secondp)
            else:
                second = '' + secondp + ''
    else:
        second = '-'
    third = str(HTLinkExteriors.identify(M))
    if third != 'False':
        third = third[0:-5]
    else:
        third = '-'
    fourth = str(OrientableCuspedCensus.identify(M))
    if fourth != 'False':
        fourth = fourth[0:-5]
    else:
        fourth = '-'
    allnames = first+', ' +secondp+', '+third+', '+fourth

    nz = load('results/' + firstprime + '_invariants.sobj')
    numfield = str(nz[1][5])
    shapes = nz[1][6]
    A = str(nz[1][0])
    B = str(nz[1][1])
    nu = str(nz[1][2]) + '^T'
    f = str(nz[1][3]) + '^T'
    fp = str(nz[1][4]) + '^T'
    oneloop = str(nz[0][0])
    twoloop = str(nz[0][1])
    threeloop = str(nz[0][2])

    template = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/Knot_Data_Template7.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("allnames",allnames)
    newdata = newdata.replace("secondname",second)
    newdata = newdata.replace("thirdname",third)
    newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(shapes[0]))
    newdata = newdata.replace("shape2",str(shapes[1]))
    newdata = newdata.replace("shape3",str(shapes[2]))
    newdata = newdata.replace("shape4",str(shapes[3]))
    newdata = newdata.replace("shape5",str(shapes[4]))
    newdata = newdata.replace("shape6",str(shapes[5]))
    newdata = newdata.replace("shape7",str(shapes[6]))
    newdata = newdata.replace("selroot",str(rootslist[index])[0:-3] + str(rootslist[index])[-2:len(rootslist[index])])
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)

    htmlout = open('/Users/2kak7/Dropbox/University/Georgia Tech/Website/Current/Stavros/Knot_Data/K7/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

    index = index + 1

rootsfile.close()
