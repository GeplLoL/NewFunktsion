from module1 import *
valeIsikukood=[]
õigeIsikukood=[]
haigla=[]
isikukoodi=[]
arvud=[]
while True:
    isikukood=input("Sisse ikood: ")
    if pikkus(isikukood)==False:
        print("4to-to ne tak")
        valeIsikukood.append(isikukood)
    else:
        jaa=kontrollnr(isikukood)
        if jaa==False:
            print("4to-to ne tak")
            valeIsikukood.append(isikukood)
        print("11 sümbolid")
        s=sugu(isikukood)
        sunni=sünnipäev(isikukood)
        kui=kuu(isikukood)
        paev=päev(isikukood)
        koht=sunnikoht(isikukood)
        print(f"{s}, {sunni}.{kui}.{paev} ,{koht}, {jaa}")
        õigeIsikukood.append(isikukood)
        haigla.append(koht)
    valeIsikukood.sort()
    õigeIsikukood.sort()
    haigla.sort()
    print("Vale isikukood", valeIsikukood)
    print("Õige isikukood", õigeIsikukood)
    print("Haigla", haigla)
