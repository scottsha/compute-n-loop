from collections import OrderedDict
 
prev = OrderedDict()

def useful_polylogs(n, z):
    if n == 1:
        return -ln(1-z)
    if n == 0:
        return z/(1-z)
    if n == -1:
        return z/(z**2 - 2*z + 1)
    if n == -2:
        return (-z**2 - z)/(z**3 - 3*z**2 + 3*z - 1)
    if n == -3:
        return (z**3 + 4*z**2 + z)/(z**4 - 4*z**3 + 6*z**2 - 4*z + 1)
    if n == -4:
        return (-z**4 - 11*z**3 - 11*z**2 - z)/(z**5 - 5*z**4 + 10*z**3 - 10*z**2 + 5*z - 1)
    if n == -5:
        return (z**5 + 26*z**4 + 66*z**3 + 26*z**2 + z)/(z**6 - 6*z**5 + 15*z**4 - 20*z**3 + 15*z**2 - 6*z + 1)
    if n == -6:
        return (-z**6 - 57*z**5 - 302*z**4 - 302*z**3 - 57*z**2 - z)/(z**7 - 7*z**6 + 21*z**5 - 35*z**4 + 35*z**3 - 21*z**2 + 7*z - 1)
    if n == -7:
        return (z**7 + 120*z**6 + 1191*z**5 + 2416*z**4 + 1191*z**3 + 120*z**2 + z)/(z**8 - 8*z**7 + 28*z**6 - 56*z**5 + 70*z**4 - 56*z**3 + 28*z**2 - 8*z + 1)
    if n == -8:
        return (-z**8 - 247*z**7 - 4293*z**6 - 15619*z**5 - 15619*z**4 - 4293*z**3 - 247*z**2 - z)/(z**9 - 9*z**8 + 36*z**7 - 84*z**6 + 126*z**5 - 126*z**4 + 84*z**3 - 36*z**2 + 9*z - 1)
    if n == -9:
        return (z**9 + 502*z**8 + 14608*z**7 + 88234*z**6 + 156190*z**5 + 88234*z**4 + 14608*z**3 + 502*z**2 + z)/(z**10 - 10*z**9 + 45*z**8 - 120*z**7 + 210*z**6 - 252*z**5 + 210*z**4 - 120*z**3 + 45*z**2 - 10*z + 1)
    if n == -10:
        return (-z**10 - 1013*z**9 - 47840*z**8 - 455192*z**7 - 1310354*z**6 - 1310354*z**5 - 455192*z**4 - 47840*z**3 - 1013*z**2 - z)/(z**11 - 11*z**10 + 55*z**9 - 165*z**8 + 330*z**7 - 462*z**6 + 462*z**5 - 330*z**4 + 165*z**3 - 55*z**2 + 11*z - 1)
    if n == -11:
        return (z**11 + 2036*z**10 + 152637*z**9 + 2203488*z**8 + 9738114*z**7 + 15724248*z**6 + 9738114*z**5 + 2203488*z**4 + 152637*z**3 + 2036*z**2 + z)/(z**12 - 12*z**11 + 66*z**10 - 220*z**9 + 495*z**8 - 792*z**7 + 924*z**6 - 792*z**5 + 495*z**4 - 220*z**3 + 66*z**2 - 12*z + 1)
    if n == -12:
        return (-z**12 - 4083*z**11 - 478271*z**10 - 10187685*z**9 - 66318474*z**8 - 162512286*z**7 - 162512286*z**6 - 66318474*z**5 - 10187685*z**4 - 478271*z**3 - 4083*z**2 - z)/(z**13 - 13*z**12 + 78*z**11 - 286*z**10 + 715*z**9 - 1287*z**8 + 1716*z**7 - 1716*z**6 + 1287*z**5 - 715*z**4 + 286*z**3 - 78*z**2 + 13*z - 1)
    if n == -13:
        return (z**13 + 8178*z**12 + 1479726*z**11 + 45533450*z**10 + 423281535*z**9 + 1505621508*z**8 + 2275172004*z**7 + 1505621508*z**6 + 423281535*z**5 + 45533450*z**4 + 1479726*z**3 + 8178*z**2 + z)/(z**14 - 14*z**13 + 91*z**12 - 364*z**11 + 1001*z**10 - 2002*z**9 + 3003*z**8 - 3432*z**7 + 3003*z**6 - 2002*z**5 + 1001*z**4 - 364*z**3 + 91*z**2 - 14*z + 1)
    if n == -14:
        return (-z**14 - 16369*z**13 - 4537314*z**12 - 198410786*z**11 - 2571742175*z**10 - 12843262863*z**9 - 27971176092*z**8 - 27971176092*z**7 - 12843262863*z**6 - 2571742175*z**5 - 198410786*z**4 - 4537314*z**3 - 16369*z**2 - z)/(z**15 - 15*z**14 + 105*z**13 - 455*z**12 + 1365*z**11 - 3003*z**10 + 5005*z**9 - 6435*z**8 + 6435*z**7 - 5005*z**6 + 3003*z**5 - 1365*z**4 + 455*z**3 - 105*z**2 + 15*z - 1)
    if n == -15:
        return (z**15 + 32752*z**14 + 13824739*z**13 + 848090912*z**12 + 15041229521*z**11 + 102776998928*z**10 + 311387598411*z**9 + 447538817472*z**8 + 311387598411*z**7 + 102776998928*z**6 + 15041229521*z**5 + 848090912*z**4 + 13824739*z**3 + 32752*z**2 + z)/(z**16 - 16*z**15 + 120*z**14 - 560*z**13 + 1820*z**12 - 4368*z**11 + 8008*z**10 - 11440*z**9 + 12870*z**8 - 11440*z**7 + 8008*z**6 - 4368*z**5 + 1820*z**4 - 560*z**3 + 120*z**2 - 16*z + 1)
    if n == -16:
        return (-z**16 - 65519*z**15 - 41932745*z**14 - 3572085255*z**13 - 85383238549*z**12 - 782115518299*z**11 - 3207483178157*z**10 - 6382798925475*z**9 - 6382798925475*z**8 - 3207483178157*z**7 - 782115518299*z**6 - 85383238549*z**5 - 3572085255*z**4 - 41932745*z**3 - 65519*z**2 - z)/(z**17 - 17*z**16 + 136*z**15 - 680*z**14 + 2380*z**13 - 6188*z**12 + 12376*z**11 - 19448*z**10 + 24310*z**9 - 24310*z**8 + 19448*z**7 - 12376*z**6 + 6188*z**5 - 2380*z**4 + 680*z**3 - 136*z**2 + 17*z - 1)
    if n == -17:
        return (z**17 + 131054*z**16 + 126781020*z**15 + 14875399450*z**14 + 473353301060*z**13 + 5717291972382*z**12 + 31055652948388*z**11 + 83137223185370*z**10 + 114890380658550*z**9 + 83137223185370*z**8 + 31055652948388*z**7 + 5717291972382*z**6 + 473353301060*z**5 + 14875399450*z**4 + 126781020*z**3 + 131054*z**2 + z)/(z**18 - 18*z**17 + 153*z**16 - 816*z**15 + 3060*z**14 - 8568*z**13 + 18564*z**12 - 31824*z**11 + 43758*z**10 - 48620*z**9 + 43758*z**8 - 31824*z**7 + 18564*z**6 - 8568*z**5 + 3060*z**4 - 816*z**3 + 153*z**2 - 18*z + 1)
    if n == -18:
        return (-z**18 - 262125*z**17 - 382439924*z**16 - 61403313100*z**15 - 2575022097600*z**14 - 40457344748072*z**13 - 285997074307300*z**12 - 1006709967915228*z**11 - 1865385657780650*z**10 - 1865385657780650*z**9 - 1006709967915228*z**8 - 285997074307300*z**7 - 40457344748072*z**6 - 2575022097600*z**5 - 61403313100*z**4 - 382439924*z**3 - 262125*z**2 - z)/(z**19 - 19*z**18 + 171*z**17 - 969*z**16 + 3876*z**15 - 11628*z**14 + 27132*z**13 - 50388*z**12 + 75582*z**11 - 92378*z**10 + 92378*z**9 - 75582*z**8 + 50388*z**7 - 27132*z**6 + 11628*z**5 - 3876*z**4 + 969*z**3 - 171*z**2 + 19*z - 1)
    if n == -19:
        return (z**19 + 524268*z**18 + 1151775897*z**17 + 251732291184*z**16 + 13796160184500*z**15 + 278794377854832*z**14 + 2527925001876036*z**13 + 11485644635009424*z**12 + 27862280567093358*z**11 + 37307713155613000*z**10 + 27862280567093358*z**9 + 11485644635009424*z**8 + 2527925001876036*z**7 + 278794377854832*z**6 + 13796160184500*z**5 + 251732291184*z**4 + 1151775897*z**3 + 524268*z**2 + z)/(z**20 - 20*z**19 + 190*z**18 - 1140*z**17 + 4845*z**16 - 15504*z**15 + 38760*z**14 - 77520*z**13 + 125970*z**12 - 167960*z**11 + 184756*z**10 - 167960*z**9 + 125970*z**8 - 77520*z**7 + 38760*z**6 - 15504*z**5 + 4845*z**4 - 1140*z**3 + 190*z**2 - 20*z + 1)