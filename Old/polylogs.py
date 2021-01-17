from collections import OrderedDict
z_poly = var('z_poly')
polylog_dict = [#Li_1
                gp(-ln(1-z_poly)),
                #Li_0
                gp(z_poly/(1-z_poly)),
                #Li_{-1}
                gp(z_poly/(z_poly**2 - 2*z_poly + 1)),
                #Li_{-2}
                gp((-z_poly**2 - z_poly)/(z_poly**3 - 3*z_poly**2 + 3*z_poly - 1)),
                #Li_{-3}
                gp((z_poly**3 + 4*z_poly**2 + z_poly)/(z_poly**4 - 4*z_poly**3 + 6*z_poly**2 - 4*z_poly + 1)),
                #Li_{-4}
                gp((-z_poly**4 - 11*z_poly**3 - 11*z_poly**2 - z_poly)/(z_poly**5 - 5*z_poly**4 + 10*z_poly**3 - 10*z_poly**2 + 5*z_poly - 1)),
                #Li_{-5}
                gp((z_poly**5 + 26*z_poly**4 + 66*z_poly**3 + 26*z_poly**2 + z_poly)/(z_poly**6 - 6*z_poly**5 + 15*z_poly**4 - 20*z_poly**3 + 15*z_poly**2 - 6*z_poly + 1)),
                #Li_{-6}
                gp((-z_poly**6 - 57*z_poly**5 - 302*z_poly**4 - 302*z_poly**3 - 57*z_poly**2 - z_poly)/(z_poly**7 - 7*z_poly**6 + 21*z_poly**5 - 35*z_poly**4 + 35*z_poly**3 - 21*z_poly**2 + 7*z_poly - 1)),
                #Li_{-7}
                gp((z_poly**7 + 120*z_poly**6 + 1191*z_poly**5 + 2416*z_poly**4 + 1191*z_poly**3 + 120*z_poly**2 + z_poly)/(z_poly**8 - 8*z_poly**7 + 28*z_poly**6 - 56*z_poly**5 + 70*z_poly**4 - 56*z_poly**3 + 28*z_poly**2 - 8*z_poly + 1)),
                #Li_{-8}
                gp((-z_poly**8 - 247*z_poly**7 - 4293*z_poly**6 - 15619*z_poly**5 - 15619*z_poly**4 - 4293*z_poly**3 - 247*z_poly**2 - z_poly)/(z_poly**9 - 9*z_poly**8 + 36*z_poly**7 - 84*z_poly**6 + 126*z_poly**5 - 126*z_poly**4 + 84*z_poly**3 - 36*z_poly**2 + 9*z_poly - 1)),
                #Li_{-9}
                gp((z_poly**9 + 502*z_poly**8 + 14608*z_poly**7 + 88234*z_poly**6 + 156190*z_poly**5 + 88234*z_poly**4 + 14608*z_poly**3 + 502*z_poly**2 + z_poly)/(z_poly**10 - 10*z_poly**9 + 45*z_poly**8 - 120*z_poly**7 + 210*z_poly**6 - 252*z_poly**5 + 210*z_poly**4 - 120*z_poly**3 + 45*z_poly**2 - 10*z_poly + 1)),
                #Li_{-10}
                gp((-z_poly**10 - 1013*z_poly**9 - 47840*z_poly**8 - 455192*z_poly**7 - 1310354*z_poly**6 - 1310354*z_poly**5 - 455192*z_poly**4 - 47840*z_poly**3 - 1013*z_poly**2 - z_poly)/(z_poly**11 - 11*z_poly**10 + 55*z_poly**9 - 165*z_poly**8 + 330*z_poly**7 - 462*z_poly**6 + 462*z_poly**5 - 330*z_poly**4 + 165*z_poly**3 - 55*z_poly**2 + 11*z_poly - 1)),
                #Li_{-11}
                gp((z_poly**11 + 2036*z_poly**10 + 152637*z_poly**9 + 2203488*z_poly**8 + 9738114*z_poly**7 + 15724248*z_poly**6 + 9738114*z_poly**5 + 2203488*z_poly**4 + 152637*z_poly**3 + 2036*z_poly**2 + z_poly)/(z_poly**12 - 12*z_poly**11 + 66*z_poly**10 - 220*z_poly**9 + 495*z_poly**8 - 792*z_poly**7 + 924*z_poly**6 - 792*z_poly**5 + 495*z_poly**4 - 220*z_poly**3 + 66*z_poly**2 - 12*z_poly + 1)),
                #Li_{-12}
                gp((-z_poly**12 - 4083*z_poly**11 - 478271*z_poly**10 - 10187685*z_poly**9 - 66318474*z_poly**8 - 162512286*z_poly**7 - 162512286*z_poly**6 - 66318474*z_poly**5 - 10187685*z_poly**4 - 478271*z_poly**3 - 4083*z_poly**2 - z_poly)/(z_poly**13 - 13*z_poly**12 + 78*z_poly**11 - 286*z_poly**10 + 715*z_poly**9 - 1287*z_poly**8 + 1716*z_poly**7 - 1716*z_poly**6 + 1287*z_poly**5 - 715*z_poly**4 + 286*z_poly**3 - 78*z_poly**2 + 13*z_poly - 1)),
                #Li_{-13}
                gp((z_poly**13 + 8178*z_poly**12 + 1479726*z_poly**11 + 45533450*z_poly**10 + 423281535*z_poly**9 + 1505621508*z_poly**8 + 2275172004*z_poly**7 + 1505621508*z_poly**6 + 423281535*z_poly**5 + 45533450*z_poly**4 + 1479726*z_poly**3 + 8178*z_poly**2 + z_poly)/(z_poly**14 - 14*z_poly**13 + 91*z_poly**12 - 364*z_poly**11 + 1001*z_poly**10 - 2002*z_poly**9 + 3003*z_poly**8 - 3432*z_poly**7 + 3003*z_poly**6 - 2002*z_poly**5 + 1001*z_poly**4 - 364*z_poly**3 + 91*z_poly**2 - 14*z_poly + 1)),
                #Li_{-14}
                gp((-z_poly**14 - 16369*z_poly**13 - 4537314*z_poly**12 - 198410786*z_poly**11 - 2571742175*z_poly**10 - 12843262863*z_poly**9 - 27971176092*z_poly**8 - 27971176092*z_poly**7 - 12843262863*z_poly**6 - 2571742175*z_poly**5 - 198410786*z_poly**4 - 4537314*z_poly**3 - 16369*z_poly**2 - z_poly)/(z_poly**15 - 15*z_poly**14 + 105*z_poly**13 - 455*z_poly**12 + 1365*z_poly**11 - 3003*z_poly**10 + 5005*z_poly**9 - 6435*z_poly**8 + 6435*z_poly**7 - 5005*z_poly**6 + 3003*z_poly**5 - 1365*z_poly**4 + 455*z_poly**3 - 105*z_poly**2 + 15*z_poly - 1)),
                #Li_{-15}
                gp((z_poly**15 + 32752*z_poly**14 + 13824739*z_poly**13 + 848090912*z_poly**12 + 15041229521*z_poly**11 + 102776998928*z_poly**10 + 311387598411*z_poly**9 + 447538817472*z_poly**8 + 311387598411*z_poly**7 + 102776998928*z_poly**6 + 15041229521*z_poly**5 + 848090912*z_poly**4 + 13824739*z_poly**3 + 32752*z_poly**2 + z_poly)/(z_poly**16 - 16*z_poly**15 + 120*z_poly**14 - 560*z_poly**13 + 1820*z_poly**12 - 4368*z_poly**11 + 8008*z_poly**10 - 11440*z_poly**9 + 12870*z_poly**8 - 11440*z_poly**7 + 8008*z_poly**6 - 4368*z_poly**5 + 1820*z_poly**4 - 560*z_poly**3 + 120*z_poly**2 - 16*z_poly + 1)),
                #Li_{-16}
                gp((-z_poly**16 - 65519*z_poly**15 - 41932745*z_poly**14 - 3572085255*z_poly**13 - 85383238549*z_poly**12 - 782115518299*z_poly**11 - 3207483178157*z_poly**10 - 6382798925475*z_poly**9 - 6382798925475*z_poly**8 - 3207483178157*z_poly**7 - 782115518299*z_poly**6 - 85383238549*z_poly**5 - 3572085255*z_poly**4 - 41932745*z_poly**3 - 65519*z_poly**2 - z_poly)/(z_poly**17 - 17*z_poly**16 + 136*z_poly**15 - 680*z_poly**14 + 2380*z_poly**13 - 6188*z_poly**12 + 12376*z_poly**11 - 19448*z_poly**10 + 24310*z_poly**9 - 24310*z_poly**8 + 19448*z_poly**7 - 12376*z_poly**6 + 6188*z_poly**5 - 2380*z_poly**4 + 680*z_poly**3 - 136*z_poly**2 + 17*z_poly - 1)),
                #Li_{-17}
                gp((z_poly**17 + 131054*z_poly**16 + 126781020*z_poly**15 + 14875399450*z_poly**14 + 473353301060*z_poly**13 + 5717291972382*z_poly**12 + 31055652948388*z_poly**11 + 83137223185370*z_poly**10 + 114890380658550*z_poly**9 + 83137223185370*z_poly**8 + 31055652948388*z_poly**7 + 5717291972382*z_poly**6 + 473353301060*z_poly**5 + 14875399450*z_poly**4 + 126781020*z_poly**3 + 131054*z_poly**2 + z_poly)/(z_poly**18 - 18*z_poly**17 + 153*z_poly**16 - 816*z_poly**15 + 3060*z_poly**14 - 8568*z_poly**13 + 18564*z_poly**12 - 31824*z_poly**11 + 43758*z_poly**10 - 48620*z_poly**9 + 43758*z_poly**8 - 31824*z_poly**7 + 18564*z_poly**6 - 8568*z_poly**5 + 3060*z_poly**4 - 816*z_poly**3 + 153*z_poly**2 - 18*z_poly + 1)),
                #Li_{-18}
                gp((-z_poly**18 - 262125*z_poly**17 - 382439924*z_poly**16 - 61403313100*z_poly**15 - 2575022097600*z_poly**14 - 40457344748072*z_poly**13 - 285997074307300*z_poly**12 - 1006709967915228*z_poly**11 - 1865385657780650*z_poly**10 - 1865385657780650*z_poly**9 - 1006709967915228*z_poly**8 - 285997074307300*z_poly**7 - 40457344748072*z_poly**6 - 2575022097600*z_poly**5 - 61403313100*z_poly**4 - 382439924*z_poly**3 - 262125*z_poly**2 - z_poly)/(z_poly**19 - 19*z_poly**18 + 171*z_poly**17 - 969*z_poly**16 + 3876*z_poly**15 - 11628*z_poly**14 + 27132*z_poly**13 - 50388*z_poly**12 + 75582*z_poly**11 - 92378*z_poly**10 + 92378*z_poly**9 - 75582*z_poly**8 + 50388*z_poly**7 - 27132*z_poly**6 + 11628*z_poly**5 - 3876*z_poly**4 + 969*z_poly**3 - 171*z_poly**2 + 19*z_poly - 1)),
                #Li_{-19}
                gp((z_poly**19 + 524268*z_poly**18 + 1151775897*z_poly**17 + 251732291184*z_poly**16 + 13796160184500*z_poly**15 + 278794377854832*z_poly**14 + 2527925001876036*z_poly**13 + 11485644635009424*z_poly**12 + 27862280567093358*z_poly**11 + 37307713155613000*z_poly**10 + 27862280567093358*z_poly**9 + 11485644635009424*z_poly**8 + 2527925001876036*z_poly**7 + 278794377854832*z_poly**6 + 13796160184500*z_poly**5 + 251732291184*z_poly**4 + 1151775897*z_poly**3 + 524268*z_poly**2 + z_poly)/(z_poly**20 - 20*z_poly**19 + 190*z_poly**18 - 1140*z_poly**17 + 4845*z_poly**16 - 15504*z_poly**15 + 38760*z_poly**14 - 77520*z_poly**13 + 125970*z_poly**12 - 167960*z_poly**11 + 184756*z_poly**10 - 167960*z_poly**9 + 125970*z_poly**8 - 77520*z_poly**7 + 38760*z_poly**6 - 15504*z_poly**5 + 4845*z_poly**4 - 1140*z_poly**3 + 190*z_poly**2 - 20*z_poly + 1))]

prev = OrderedDict()
