from module1 import *
valeIsikukood=[]
õigeIsikukood=[]
haigla=[]
isikukoodi=[]
arvud=[]
while True: 
    isikukood=input("Sisse ikood: ")
    jaak=kontrollnumber(isikukood)
    if pikkus(isikukood)==False:
        print("4to-to ne tak")
    else:
        print("11 sümbolid")
        s=sugu(isikukood)
        if s=="viga" or jaak=="Viga":
            print("Esimene täht ei ole õige") 
            valeIsikukood.append(isikukood)
        else:
            õigeIsikukood.append(isikukood)
            print(s)
            aasta=sünnipäev(isikukood)
            mesjac=kuu(isikukood)
            paev=päev(isikukood)
            sünnikoht=sunnikoht(isikukood)
            print(jaak)
            haigla.append(sünnikoht)
            print(f"{aasta}.{mesjac}.{paev}, {sünnikoht}, {jaak}")
    arvudSort(valeIsikukood)
    arvudSort(õigeIsikukood)
    haigla.sort()
    print(f"vale isikukood, {valeIsikukood}")
    print(f"õige isikukood, {õigeIsikukood}")
    print(f"haigla, {haigla}")
    print(arvud)
    print(isikukoodi)
