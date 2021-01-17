#from snappy import *
from sage.all_cmdline import *

num_manifold = ['first', 'second', 'third', 'fourth', 'five', 'sixth', 'seventh', 'eighth', 'nineth', 'tenth', '11th', '12th', '13th',\
    '14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th',\
    '30th','31st','32nd','33rd','34th','35th','36th','37th','38th','39th',\
    '40th','41st','42nd','43rd','44th','45th','46th','47th','48th','49th',\
    '50th','51st','52nd','53rd','54th','55th','56th','57th','58th','59th',\
    '60th','61st','62nd','63rd','64th','65th','66th','67th','68th','69th',\
    '70th','71st','72nd','73rd','74th','75th','76th','77th','78th','79th',\
    '80th','81st','82nd','83rd','84th','85th','86th','87th','88th','89th',\
    '90th','91st','92nd','93rd','94th','95th','96th','97th','98th','99th',\
    '100th','101st','102nd','103rd','104th','105th','106th','107th','108th','109th',\
    '110th','111th','112th','113th','114th','115th','116th','117th','118th','119th',\
    '120th','121st','122nd','123rd','124th','125th','126th','127th','128th','129th',\
    '130th','131st','132nd','133rd','134th','135th','136th','137th','138th','139th',\
    '140th','141st','142nd','143rd','144th','145th','146th','147th','148th','149th',\
    '150th','151st','152nd','153rd','154th','155th','156th','157th','158th','159th',\
    '160th','161st','162nd','163rd','164th','165th','166th','167th','168th','169th',\
    '170th','171st','172nd','173rd','174th','175th','176th','177th','178th','179th',\
    '180th','181st','182nd','183rd','184th','185th','186th','187th','188th','189th',\
    '190th','191st','192nd','193rd','194th','195th','196th','197th','198th','199th',\
    '200th','201st','202nd','203rd','204th','205th','206th','207th','208th','209th',\
    '210th','211th','212th','213th','214th','215th','216th','217th','218th','219th',\
    '220th','221st','222nd','223rd','224th','225th','226th','227th','228th','229th',\
    '230th','231st','232nd','233rd','234th','235th','236th','237th','238th','239th',\
    '240th','241st','242nd','243rd','244th','245th','246th','247th','248th','249th',\
    '250th','251st','252nd','253rd','254th','255th','256th','257th','258th','259th',\
    '260th','261st','262nd','263rd','264th','265th','266th','267th','268th','269th',\
    '270th','271st','272nd','273rd','274th','275th','276th','277th','278th','279th',\
    '280th','281st','282nd','283rd','284th','285th','286th','287th','288th','289th',\
    '290th','291st','292nd','293rd','294th','295th','296th','297th','298th','299th',\
    '300th','301st']

#K2
for m in range(1,2):
    #M = Manifold('K2_%d' %m)
    first = 'K2_{%d}' %m
    firstprime = 'K2_%d' %m
    #second = str(LinkExteriors.identify(M))
    #if second != 'False':
    #    second = second[0:-5]
    #    if second[1] == '_':
    #        secondp = second[0:2] + '{' + second[2:len(second)] + '}'
    #        second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #    elif second[2] == '_':
    #        secondp = second[0:3] + '{' + second[3:len(second)] + '}'
    #        if int(second[0:2]) <= 10:
    #            second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #        else:
    #            second = '\(' + secondp + '\)'
    #else:
    #    second = '\(-\)'
    #third = str(HTLinkExteriors.identify(M))
    #if third != 'False':
    #    third = third[0:-5]
    #else:
    #    third = '-'
    #fourth = str(OrientableCuspedCensus.identify(M))
    #if fourth != 'False':
    #    fourth = fourth[0:-5]
    #else:
    #    fourth = '-'
    #allnames = first+', ' +secondp+', '+third+', '+fourth

    resultfile = load('../results/CensusKnots/2T/' + firstprime + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))
    fiveloop = str(latex(resultfile[0][4]))
    sixloop = str(latex(resultfile[0][5]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template2.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[m-1])
    #newdata = newdata.replace("allnames",allnames)
    #newdata = newdata.replace("secondname",second)
    #newdata = newdata.replace("thirdname",third)
    #newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("selroot",root)
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
    newdata = newdata.replace("sixloop",sixloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/2T/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#K3
for m in range(1,3):
    #M = Manifold('K3_%d' %m)
    first = 'K3_{%d}' %m
    firstprime = 'K3_%d' %m
    # second = str(LinkExteriors.identify(M))
    # if second != 'False':
    #     second = second[0:-5]
    #     if second[1] == '_':
    #         secondp = second[0:2] + '{' + second[2:len(second)] + '}'
    #         second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #     elif second[2] == '_':
    #         secondp = second[0:3] + '{' + second[3:len(second)] + '}'
    #         if int(second[0:2]) <= 10:
    #             second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #         else:
    #             second = '\(' + secondp + '\)'
    # else:
    #     second = '\(-\)'
    # third = str(HTLinkExteriors.identify(M))
    # if third != 'False':
    #     third = third[0:-5]
    # else:
    #     third = '-'
    # fourth = str(OrientableCuspedCensus.identify(M))
    # if fourth != 'False':
    #     fourth = fourth[0:-5]
    # else:
    #     fourth = '-'
    # allnames = first+', ' +secondp+', '+third+', '+fourth

    resultfile = load('../results/CensusKnots/3T/' + firstprime + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))
    fiveloop = str(latex(resultfile[0][4]))
    sixloop = str(latex(resultfile[0][5]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template3.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[m-1])
    # newdata = newdata.replace("allnames",allnames)
    # newdata = newdata.replace("secondname",second)
    # newdata = newdata.replace("thirdname",third)
    # newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("selroot",root)
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
    newdata = newdata.replace("sixloop",sixloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/3T/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#K4
for m in range(1,5):
    #M = Manifold('K4_%d' %m)
    first = 'K4_{%d}' %m
    firstprime = 'K4_%d' %m
    # second = str(LinkExteriors.identify(M))
    # if second != 'False':
    #     second = second[0:-5]
    #     if second[1] == '_':
    #         secondp = second[0:2] + '{' + second[2:len(second)] + '}'
    #         second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #     elif second[2] == '_':
    #         secondp = second[0:3] + '{' + second[3:len(second)] + '}'
    #         if int(second[0:2]) <= 10:
    #             second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #         else:
    #             second = '\(' + secondp + '\)'
    # else:
    #     second = '\(-\)'
    # third = str(HTLinkExteriors.identify(M))
    # if third != 'False':
    #     third = third[0:-5]
    # else:
    #     third = '-'
    # fourth = str(OrientableCuspedCensus.identify(M))
    # if fourth != 'False':
    #     fourth = fourth[0:-5]
    # else:
    #     fourth = '-'
    # allnames = first+', ' +secondp+', '+third+', '+fourth

    resultfile = load('../results/CensusKnots/4T/' + firstprime + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))
    fiveloop = str(latex(resultfile[0][4]))
    sixloop = str(latex(resultfile[0][5]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template4.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[m-1])
    # newdata = newdata.replace("allnames",allnames)
    # newdata = newdata.replace("secondname",second)
    # newdata = newdata.replace("thirdname",third)
    # newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("selroot",root)
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
    newdata = newdata.replace("sixloop",sixloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/4T/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#K5
for m in range(1,23):
    #M = Manifold('K5_%d' %m)
    first = 'K5_{%d}' %m
    firstprime = 'K5_%d' %m
    # second = str(LinkExteriors.identify(M))
    # if second != 'False':
    #     second = second[0:-5]
    #     if second[1] == '_':
    #         secondp = second[0:2] + '{' + second[2:len(second)] + '}'
    #         second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #     elif second[2] == '_':
    #         secondp = second[0:3] + '{' + second[3:len(second)] + '}'
    #         if int(second[0:2]) <= 10:
    #             second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #         else:
    #             second = '\(' + secondp + '\)'
    # else:
    #     second = '\(-\)'
    # third = str(HTLinkExteriors.identify(M))
    # if third != 'False':
    #     third = third[0:-5]
    # else:
    #     third = '-'
    # fourth = str(OrientableCuspedCensus.identify(M))
    # if fourth != 'False':
    #     fourth = fourth[0:-5]
    # else:
    #     fourth = '-'
    # allnames = first+', ' +secondp+', '+third+', '+fourth

    resultfile = load('../results/CensusKnots/5T/' + firstprime + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))
    fiveloop = str(latex(resultfile[0][4]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template5.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[m-1])
    # newdata = newdata.replace("allnames",allnames)
    # newdata = newdata.replace("secondname",second)
    # newdata = newdata.replace("thirdname",third)
    # newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("selroot",root)
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

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/5T/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#K6
for m in range(1,44):
    #M = Manifold('K6_%d' %m)
    first = 'K6_{%d}' %m
    firstprime = 'K6_%d' %m
    # second = str(LinkExteriors.identify(M))
    # if second != 'False':
    #     second = second[0:-5]
    #     if second[1] == '_':
    #         secondp = second[0:2] + '{' + second[2:len(second)] + '}'
    #         second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #     elif second[2] == '_':
    #         secondp = second[0:3] + '{' + second[3:len(second)] + '}'
    #         if int(second[0:2]) <= 10:
    #             second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #         else:
    #             second = '\(' + secondp + '\)'
    # else:
    #     second = '\(-\)'
    # third = str(HTLinkExteriors.identify(M))
    # if third != 'False':
    #     third = third[0:-5]
    # else:
    #     third = '-'
    # fourth = str(OrientableCuspedCensus.identify(M))
    # if fourth != 'False':
    #     fourth = fourth[0:-5]
    # else:
    #     fourth = '-'
    # allnames = first+', ' +secondp+', '+third+', '+fourth

    resultfile = load('../results/CensusKnots/6T/' + firstprime + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template6.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[m-1])
    # newdata = newdata.replace("allnames",allnames)
    # newdata = newdata.replace("secondname",second)
    # newdata = newdata.replace("thirdname",third)
    # newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("shape6",str(latex(shapes[5])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/6T/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#K7
for m in range(1,130):
    #M = Manifold('K7_%d' %m)
    first = 'K7_{%d}' %m
    firstprime = 'K7_%d' %m
    # second = str(LinkExteriors.identify(M))
    # if second != 'False':
    #     second = second[0:-5]
    #     if second[1] == '_':
    #         secondp = second[0:2] + '{' + second[2:len(second)] + '}'
    #         second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #     elif second[2] == '_':
    #         secondp = second[0:3] + '{' + second[3:len(second)] + '}'
    #         if int(second[0:2]) <= 10:
    #             second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
    #         else:
    #             second = '\(' + secondp + '\)'
    # else:
    #     second = '\(-\)'
    # third = str(HTLinkExteriors.identify(M))
    # if third != 'False':
    #     third = third[0:-5]
    # else:
    #     third = '-'
    # fourth = str(OrientableCuspedCensus.identify(M))
    # if fourth != 'False':
    #     fourth = fourth[0:-5]
    # else:
    #     fourth = '-'
    # allnames = first+', ' +secondp+', '+third+', '+fourth

    resultfile = load('../results/CensusKnots/7T/' + firstprime + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template7.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[m-1])
    # newdata = newdata.replace("allnames",allnames)
    # newdata = newdata.replace("secondname",second)
    # newdata = newdata.replace("thirdname",third)
    # newdata = newdata.replace("fourthname",fourth)
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("shape6",str(latex(shapes[5])))
    newdata = newdata.replace("shape7",str(latex(shapes[6])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/7T/' + firstprime + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#K8
for m in range(1,302):
    if m in [35,60,63,67,69,71,81,100,107,282]:
        m;
    else:
        #M = Manifold('K8_%d' %m)
        first = 'K8_{%d}' %m
        firstprime = 'K8_%d' %m
        # second = str(LinkExteriors.identify(M))
        # if second != 'False':
        #     second = second[0:-5]
        #     if second[1] == '_':
        #         secondp = second[0:2] + '{' + second[2:len(second)] + '}'
        #         second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
        #     elif second[2] == '_':
        #         secondp = second[0:3] + '{' + second[3:len(second)] + '}'
        #         if int(second[0:2]) <= 10:
        #             second = '<a href="http://katlas.math.toronto.edu/wiki/'+'%s"><span style="font-weight: bold;">\( %s \)</span></a>' %(second, secondp)
        #         else:
        #             second = '\(' + secondp + '\)'
        # else:
        #     second = '\(-\)'
        # third = str(HTLinkExteriors.identify(M))
        # if third != 'False':
        #     third = third[0:-5]
        # else:
        #     third = '-'
        # fourth = str(OrientableCuspedCensus.identify(M))
        # if fourth != 'False':
        #     fourth = fourth[0:-5]
        # else:
        #     fourth = '-'
        # allnames = first+', ' +secondp+', '+third+', '+fourth

        resultfile = load('../results/CensusKnots/8T/' + firstprime + '_invariants.sobj')
        numfield = str(latex(resultfile[1][5]))
        shapes = resultfile[1][6]
        try:
            flag = False
            root = str(latex(resultfile[1][7]))[15:-4] + 'I'
            if root[0] == '-':
                root = '-' + root[2:]
            if root[0] == '.':
                root = '0' + root
                flag = True
            else:
                root = root[2:]
            if flag == True:
                if root[22] == '-':
                    root = root[:19] + ' - ' + root[26:]
                else:
                    root = root[:19] + ' + ' + root[26:]
            else:
                if root[23] == '-':
                    root = root[:18] + ' - ' + root[25:]
                else:
                    root = root[:18] + ' + ' + root[25:]
        except:
            root = '-'
        A = str(latex(resultfile[1][0]))
        B = str(latex(resultfile[1][1]))
        nu = str(latex(resultfile[1][2])) + '^T'
        f = str(latex(resultfile[1][3])) + '^T'
        fp = str(latex(resultfile[1][4])) + '^T'
        oneloop = str(latex(resultfile[0][0]))
        twoloop = str(latex(resultfile[0][1]))
        threeloop = str(latex(resultfile[0][2]))
        threeloop = str(latex(resultfile[0][3]))

        template = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/Knot_Data_Template8.html','r')
        filedata = template.read()
        template.close()

        newdata = filedata.replace("knotname",first)
        newdata = newdata.replace("knottype",firstprime)
        newdata = newdata.replace("nummanifold",num_manifold[m-1])
        # newdata = newdata.replace("allnames",allnames)
        # newdata = newdata.replace("secondname",second)
        # newdata = newdata.replace("thirdname",third)
        # newdata = newdata.replace("fourthname",fourth)
        newdata = newdata.replace("polyhere",numfield)
        newdata = newdata.replace("shape1",str(latex(shapes[0])))
        newdata = newdata.replace("shape2",str(latex(shapes[1])))
        newdata = newdata.replace("shape3",str(latex(shapes[2])))
        newdata = newdata.replace("shape4",str(latex(shapes[3])))
        newdata = newdata.replace("shape5",str(latex(shapes[4])))
        newdata = newdata.replace("shape6",str(latex(shapes[5])))
        newdata = newdata.replace("shape7",str(latex(shapes[6])))
        newdata = newdata.replace("shape8",str(latex(shapes[7])))
        newdata = newdata.replace("selroot",root)
        newdata = newdata.replace("matrixA",A)
        newdata = newdata.replace("matrixB",B)
        newdata = newdata.replace("nuhere",nu)
        newdata = newdata.replace("fhere",f)
        newdata = newdata.replace("fphere",fp)
        newdata = newdata.replace("oneloop",oneloop)
        newdata = newdata.replace("twoloop",twoloop)
        newdata = newdata.replace("threeloop",threeloop)
        newdata = newdata.replace("fourloop",fourloop)

        htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/CensusKnots/8T/' + firstprime + '.html','w')
        htmlout.write(newdata)
        htmlout.close()

## Link Exteriors
#2T
all_2T = ['4_1']
current_2T = []
current_2T_LaTeX = []
for m in range(len(current_2T)):
    first = current_2T[m]
    firstprime = current_2T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/2T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template2.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_2T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/2T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#3T
all_3T = ['5_2']
current_3T = []
current_3T_LaTeX = []
for m in range(len(current_3T)):
    first = current_3T[m]
    firstprime = current_3T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/3T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template3.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_3T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/3T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#4T
all_4T = ['6_1', '7_2']
current_4T = []
current_4T_LaTeX = []
for m in range(len(current_4T)):
    first = current_4T[m]
    firstprime = current_4T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/4T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template4.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_4T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/4T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#5T
all_5T = ['6_2', '7_3', '8_1', '8_20', '9_2', '9_42', '9_46', '10_132', '10_139', '11_190']
current_5T = ['8_1', '8_20', '9_2', '9_42', '9_46']
current_5T_LaTeX = ['8_1', '8_{20}', '9_2', '9_{42}', '9_{46}']
for m in range(len(current_5T)):
    first = current_5T[m]
    firstprime = current_5T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/5T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template5.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_5T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/5T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#6T
all_6T = ['6_3', '7_4', '8_2', '8_3', '8_4', '9_3', '9_4', '10_1', '10_125',\
        '10_140', '10_145', '11_276', '11_278', '11_552']
current_6T = ['8_2', '8_3', '8_4', '9_3', '9_4']
current_6T_LaTeX = ['8_2', '8_3', '8_4', '9_3', '9_4']
for m in range(len(current_6T)):
    first = current_6T[m]
    firstprime = current_6T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/6T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template6.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_6T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("shape6",str(latex(shapes[5])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/6T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#7T
all_7T = ['7_5', '8_21', '9_5', '9_43', '10_2', '10_3', '10_4', '10_8', '10_128',\
        '10_161', '10_162', '11_155', '11_251', '11_547', '11_550', '11_551']
current_7T = ['8_21', '9_5', '9_43']
current_7T_LaTeX = ['8_{21}', '9_5', '9_{43}']
for m in range(len(current_7T)):
    first = current_7T[m]
    firstprime = current_7T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/7T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template7.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_7T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("shape6",str(latex(shapes[5])))
    newdata = newdata.replace("shape7",str(latex(shapes[6])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/7T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#8T
all_8T = ['7_6', '7_7', '8_5', '8_6', '8_7', '8_9', '9_6', '9_44', '10_126',\
        '10_130', '10_142', '10_153', '11_182', '11_233', '11_247', '11_266',\
        '11_270', '11_274', '11_298', '11_537', '11_548']
current_8T = ['8_5', '8_6', '8_7', '8_9', '9_6', '9_44']
current_8T_LaTeX = ['8_5', '8_6', '8_7', '8_9', '9_6', '9_{44}']
for m in range(len(current_8T)):
    first = current_8T[m]
    firstprime = current_8T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/8T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template8.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_8T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("shape6",str(latex(shapes[5])))
    newdata = newdata.replace("shape7",str(latex(shapes[6])))
    newdata = newdata.replace("shape8",str(latex(shapes[7])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/8T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()

#9T
all_9T = ['8_8', '8_10', '8_11', '8_13', '9_7', '9_8', '9_9', '9_10', '9_11',\
        '9_35', '9_45', '10_5', '10_6', '10_9', '10_20', '10_46', '10_133',\
        '10_134', '10_136', '10_141', '10_152', '11_141', '11_179', '11_188',\
        '11_225', '11_262', '11_333', '11_353', '11_549']
current_9T = ['8_8', '8_10', '8_11', '8_13', '9_7', '9_8', '9_9', '9_10', '9_11',\
            '9_35', '9_45']
current_9T_LaTeX = ['8_8', '8_{10}', '8_{11}', '8_{13}', '9_7', '9_8', '9_9',\
             '9_{10}', '9_{11}', '9_{35}', '9_{45}']
for m in range(len(current_9T)):
    first = current_9T[m]
    firstprime = current_9T_LaTeX[m]
    resultfile = load('../results/LinkExteriors/9T/' + first + '_invariants.sobj')
    numfield = str(latex(resultfile[1][5]))
    shapes = resultfile[1][6]
    try:
        flag = False
        root = str(latex(resultfile[1][7]))[15:-4] + 'I'
        if root[0] == '-':
            root = '-' + root[2:]
        if root[0] == '.':
            root = '0' + root
            flag = True
        else:
            root = root[2:]
        if flag == True:
            if root[22] == '-':
                root = root[:19] + ' - ' + root[26:]
            else:
                root = root[:19] + ' + ' + root[26:]
        else:
            if root[23] == '-':
                root = root[:18] + ' - ' + root[25:]
            else:
                root = root[:18] + ' + ' + root[25:]
    except:
        root = '-'
    A = str(latex(resultfile[1][0]))
    B = str(latex(resultfile[1][1]))
    nu = str(latex(resultfile[1][2])) + '^T'
    f = str(latex(resultfile[1][3])) + '^T'
    fp = str(latex(resultfile[1][4])) + '^T'
    oneloop = str(latex(resultfile[0][0]))
    twoloop = str(latex(resultfile[0][1]))
    threeloop = str(latex(resultfile[0][2]))
    fourloop = str(latex(resultfile[0][3]))

    template = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/Knot_Data_Template9.html','r')
    filedata = template.read()
    template.close()

    newdata = filedata.replace("knotname",first)
    newdata = newdata.replace("knottype",firstprime)
    newdata = newdata.replace("nummanifold",num_manifold[all_9T.index(first)])
    newdata = newdata.replace("polyhere",numfield)
    newdata = newdata.replace("shape1",str(latex(shapes[0])))
    newdata = newdata.replace("shape2",str(latex(shapes[1])))
    newdata = newdata.replace("shape3",str(latex(shapes[2])))
    newdata = newdata.replace("shape4",str(latex(shapes[3])))
    newdata = newdata.replace("shape5",str(latex(shapes[4])))
    newdata = newdata.replace("shape6",str(latex(shapes[5])))
    newdata = newdata.replace("shape7",str(latex(shapes[6])))
    newdata = newdata.replace("shape8",str(latex(shapes[7])))
    newdata = newdata.replace("shape9",str(latex(shapes[8])))
    newdata = newdata.replace("selroot",root)
    newdata = newdata.replace("matrixA",A)
    newdata = newdata.replace("matrixB",B)
    newdata = newdata.replace("nuhere",nu)
    newdata = newdata.replace("fhere",f)
    newdata = newdata.replace("fphere",fp)
    newdata = newdata.replace("oneloop",oneloop)
    newdata = newdata.replace("twoloop",twoloop)
    newdata = newdata.replace("threeloop",threeloop)
    newdata = newdata.replace("fourloop",fourloop)

    htmlout = open('../../University/Georgia Tech/Website/Current/Knot_Data/LinkExteriors/9T/' + first + '.html','w')
    htmlout.write(newdata)
    htmlout.close()
