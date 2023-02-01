from module1 import *
while True: 
    isikukood=input("Sisse ikood: ")
    if pikkus(isikukood)==False:
        print("4to-to ne tak")
    else:
        print("11 sümbolid")
        s=sugu(isikukood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            print(s)
            aasta=sünnipäev(isikukood)
            mesjac=kuu(isikukood)
            paev=päev(isikukood)
            print(f"{aasta}.{mesjac}.{paev}")
            