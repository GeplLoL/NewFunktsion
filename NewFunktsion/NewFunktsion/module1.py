def pikkus(isikukood:str):
    """Funktsioon tagastab True, kui pikkus on 11
     sümbolid
     :param str isikukood: Inimese isikukood
     :rtype:bool
    """
    if len(isikukood)==11:
        flag=True
    else:
        flag=False
    return flag
def sugu(isikukood:str)->str:
    """kui esimene täht on [1,2,3,4,5,6], siis
      määrame sugu
    :param str isikukood:Isikukood
    :rtype:str
    """
    listIsikukood=list(map(int,isikukood))
    if listIsikukood[0] in [1,3,5]:
        s="mees"
    elif listIsikukood[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s
def sünnipäev(isikukood:str)->str:
    """kui esimene täht on [1,2,3,4,5,6], siis
      määrame sünnipäev
    :param str isikukood:Isikukood
    :rtype:str
    """
    listIsikukood=list(isikukood)
    if listIsikukood[0] in ["1","2"]:
        s="18"
        xy=s+listIsikukood[1]+listIsikukood[2]
    elif listIsikukood[0] in ["3","4"]:
        s="19"
        xy=s+listIsikukood[1]+listIsikukood[2]
    elif listIsikukood[0] in ["5","6"]:
        s="20"
        xy=s+listIsikukood[1]+listIsikukood[2]
    else:
        s="viga"
    return xy
def kuu(isikukood:str)->str:
    """kui esimene täht on [1,2,3,4,5,6], siis
      määrame sünnipäev
    :param str isikukood:Isikukood
    :rtype:str
    """
    listIsikukood=list(isikukood)
    if  listIsikukood[3] in ["0"] and listIsikukood[4] in ["1","2","3","4","5","6","7","8","9"]:
        kue=listIsikukood[3]+listIsikukood[4]
    elif listIsikukood[3] in ["1"] and listIsikukood[4] in ["0","1","2"]:
        kue=listIsikukood[3]+listIsikukood[4]
    else:
        kue="neljas täht 0-9 and kolmas 0-1"
    return kue
def päev(isikukood:str)->str:
    """kui esimene täht on [1,2,3,4,5,6], siis
      määrame sünnipäev
    :param str isikukood:Isikukood
    :rtype:str
    """
    listIsikukood=list(isikukood)
    if listIsikukood[5] in ["0","1","2"] and listIsikukood[6] in ["0","1","2","3","4","5","6","7","8","9"]:
        paev=listIsikukood[5]+listIsikukood[6]
    elif listIsikukood[5] in ["3"] and listIsikukood[6] in ["0","1"]:
        paev=listIsikukood[5]+listIsikukood[6]
    else:
        paev="vies täht 0-3 and kues 0-9"
    return paev
def sunnikoht(isikukood:str)->str:
    listIsikukood=list(isikukood)
    summa=listIsikukood[7]+listIsikukood[8]+listIsikukood[9]
    summa=int(summa)
    if summa in range(1,11):
        sünnikoht="Kuressaare Haigla"
    elif summa in range(11,20):
        sünnikoht="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif summa in range(21,220):
        sünnikoht="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif summa in range(221,271):
        sünnikoht="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif summa in range(271,371):
        sünnikoht="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif summa in range(371,421):
        sünnikoht="Narva Haigla"
    elif summa in range(421,471):
        sünnikoht="Pärnu Haigla"
    elif summa in range(471,491):
        sünnikoht="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif summa in range(491,521):
        sünnikoht="Järvamaa Haigla (Paide)"
    elif summa in range(521,571):
        sünnikoht="Rakvere, Tapa haigla"
    elif summa in range(571,601):
        sünnikoht="Valga Haigla"
    elif summa in range(601,651):
        sünnikoht="Viljandi Haigla"
    elif summa in range(601,651):
        sünnikoht="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        sünnikoht="Viga koos sünnikoht"
    return sünnikoht
def kontrollnumber(isikukood:str)->str:
    """kui esimene täht on [1,2,3,4,5,6], siis
      määrame sugu
    :param str isikukood:Isikukood
    :rtype:str
    """
    astme1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    astme2=[3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    for i in range(0,11)
    x=isikukood[i]*astme1[i]
    x=x/11
    print(x)
    if x%10:
    x=isikukood[i]*astme2[i]
    x=x/11
    if x = 10:
        x="Kontrol sum:0"
    else:
        x="Viga"
    return x
