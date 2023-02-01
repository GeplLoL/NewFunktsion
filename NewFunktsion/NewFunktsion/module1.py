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
    if summa<=1 and  summa>=10:
        sünnikoht="Kuressaare Haigla"
    elif summa<=11 and  summa>=19:
        sünnikoht="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif summa<=21 and  summa>=220:
        sünnikoht="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
