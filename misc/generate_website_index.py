from snappy import *
f = open('test.txt','w')
for i in CensusKnots():
    try:
        if i.num_tetrahedra() == 9 and str(CensusKnots.identify(i)) != 'False':
            name = str(i)[:-5]
            link = str(CensusKnots.identify(i))[:-5]
            f.write('<a href="Knot_Data/9T/' + link + '.html">\(' + name + '\)</a><br/>\n')
        elif i.num_tetrahedra() == 9 and str(HTLinkExteriors.identify(i)) != 'False':
            name = str(i)[:-5]
            link = str(HTLinkExteriors.identify(i))[:-5]
            f.write('<a href="Knot_Data/9T/' + link + '.html">\(' + name + '\)</a><br/>\n')
        elif i.num_tetrahedra() == 9 and str(LinkExteriors.identify(i)) != 'False':
            name = str(i)[:-5]
            link = str(LinkExteriors.identify(i))[:-5]
            f.write('<a href="Knot_Data/9T/' + link + '.html">\(' + name + '\)</a><br/>\n')
        elif i.num_tetrahedra() == 9:
            name = str(i)[:-5]
            link = name
            f.write('<a href="Knot_Data/9T/' + link + '.html">\(' + name + '\)</a><br/>\n')
    except:
        if i.num_tetrahedra() == 9:
            name = str(i)[:-5]
            link = name
            f.write('<a href="Knot_Data/9T/' + link + '.html">\(' + name + '\)</a><br/>\n')
f.close()
