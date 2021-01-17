from snappy import *
for m in range(1,44):
    M = Manifold('K6_%d' %m)
    first = 'K6_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
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
    print first+', ' +second+', '+third+', '+fourth


for m in range(1,130):
    M = Manifold('K7_%d' %m)
    first = 'K7_%d' %m
    second = str(LinkExteriors.identify(M))
    if second != 'False':
        second = second[0:-5]
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
    print first+', ' +second+', '+third+', '+fourth
