#-----------------------
#Milan Petrovski TARpv24
#Vigade Otsing

import math #peab olema from math import * voi lihtsalt import math
print("Ruudu karakteristikud")
try:
    a=float(input("Sisesta ruudu külje pikkus => "))  # input väärtus muuda float sest alguses on str ja tuleb viga
    if a > 1:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P)  # oli vale sulgud, peab olema "" ja pole koma ( , ) aga peab olema
        di=a*math.sqrt(2)  # funktsiooni nimi oli vale sqr > sqrt 
        print("Ruudu diagonaal", round(di,2))
        print()
        print("Ristküliku karakteristikud") #kustutasin ) sest peab olema 1 sulg 
    else:
        print("Külje pikkus peab olema rohkem kui 0")
except:
    print("Sisestage ainult numbrid!")


try:
    b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # input väärtus muuda float sest alguses on str ja tuleb viga
    c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # input väärtus muuda float sest alguses on str ja tuleb viga
    if b > 0 and c > 0: 
        S=b*c
        print("Ristküliku pindala", S)  # vale sulgud tyyp ja lisasin "
        P=2*(b+c)  # puudud *
        print("Ristküliku ümbermõõt", P)
        di=math.sqrt(b ** 2 + c ** 2)
        print("Ristküliku diagonaal", round(di, 2))  # roundi lõppu lisa sulgud
        print()
        print("Ringi karakteristikud")
    else:
        print("Külje pikkus peab olema rohkem kui 0")
except:
    print("Sisestage ainult numbrid!")

try:
    r=float(input("Sisesta ringi raadiuse pikkus => "))  # vale sulgud ja peab olema float andmetyyp
    if r > 0:
        d=2*r # puudub *
        print("Ringi läbimõõt", d)
        S=math.pi*r**2 #pi pole funktsioon aga muutuja siis ei kasutame ()
        print("Ringi pindala", round(S,2))   
        C=2*math.pi*r #pi pole funktsioon aga muutuja siis ei kasutame ()
        print("Ringjoone pikkus", round(C,2))  #puudub )
    else:  
        print("Külje pikkus peab olema rohkem kui 0")
except:
    print("Sisestage ainult numbrid!")
#lisaks muuda encoding UTF8