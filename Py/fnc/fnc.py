j = [110, 1, 122, 3, 6, -100, 22, -22222]
pi = 3.141592653589793

#est tähestik
tähestik = 'abcdefghijklmnopqrsšzžtuvwõäöüxy'

#kuud
kuud = ['', 'jan', 'veb', 'mär', 'apr', 'mai', 'jun', 'jul' ,'aug', 'sept', 'okt', 'nov' ,'dets']
kuud_2 = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober",
        "november", "detsember"]

##Tabeli sorteerimine
def Vahetus_min_max(arvud):
    #Muutuja vahetuse kontrollimiseks
    has_swapped = True

    #Kui vahetus on toimunud, siis siseneb tsüklisse
    while(has_swapped):
        #Kontrollmuutuja väärtuse muutmine
        has_swapped = False

        for j in range(len(arvud) - 1):
            #Kui on element on suurem kui järgmine, siis vahetame kohad
            if arvud[j] > arvud[j+1]:
                temp = arvud[j]
                arvud[j] = arvud[j+1]
                arvud[j+1] = temp
                #Kui vahetus toimus, saab kontrollmuutuja oma väärtuseks uuesti True
                has_swapped = True
    #print("Sorteeritud list: {0}".format(arvud))
    return arvud

def Vahetus_max_min(arvud):
    #Muutuja vahetuse kontrollimiseks
    has_swapped = True

    #Kui vahetus on toimunud, siis siseneb tsüklisse
    while(has_swapped):
        #Kontrollmuutuja väärtuse muutmine
        has_swapped = False

        for j in range(len(arvud) - 1):
            #Kui on element on suurem kui järgmine, siis vahetame kohad
            if arvud[j] < arvud[j+1]:
                temp = arvud[j+1]
                arvud[j+1] = arvud[j]
                arvud[j] = temp
                #Kui vahetus toimus, saab kontrollmuutuja oma väärtuseks uuesti True
                has_swapped = True
    print("Sorteeritud list: {0}".format(arvud))
    return arvud


##Min Max
def Suurim_arv(arvud):
    '''Suurima arvu leidmine, võrdlen ühe kaupa ja suurim võidab.'''
    suurim_arv = arvud[-1]
    for i in range(len(arvud)):
        arv1 = arvud[i]
        arv2 = arvud[len(arvud)-1]
        i +=1
        if arv1 > arv2:
            if arv1 > suurim_arv:
                suurim_arv = arv1
        elif arv2 > arv1:
            if arv2 > suurim_arv:
                suurim_arv = arv2
    return suurim_arv

def Vähim_arv(arvud):
    '''Kõige väiksema arvu leidmine, võrdlen ühe kaupa ja vähim võidab.'''
    vähim_arv = arvud[-1]
    for i in range(len(arvud)):
        arv1 = arvud[i]
        arv2 = arvud[len(arvud)-1]
        if arv1 < arv2:
            if arv1 < vähim_arv:
                vähim_arv = arv1
        elif arv2 < arv1:
            if arv2 < vähim_arv:
                vähim_arv = arv2
    return vähim_arv

##Keskmine, ümardamine, abs
def Keskmine(arvud):
    '''Keskmise arvu leidmine'''
    keskmine = 0
    for i in range(len(arvud)):
        keskmine += arvud[i]
    keskmine /= len(arvud)
    return keskmine

def Ümarda(n, kohta=0):
    '''Ümardamis funktsioon:
    n -- arv, mida tahad ümardada. 
    kohta -- positiivsed arvud on mitu kohta peale koma,
    negatiivsed arvud on mitu kohta enne koma.'''
    if n > 0:
        kordaja = 10 ** kohta
        uus_arv = int(n * kordaja + 0.5) / kordaja
    elif n < 0:
        kordaja = 10 ** kohta
        uus_arv = int(n * kordaja - 0.5) / kordaja
    return uus_arv

def Absoluut_väärtus(arv):
    if arv > 0:
        arv_uus = arv
    elif arv < 0:
        arv_uus = (-1) * arv
    return arv_uus

##Summeerimine
def Summeerimine(algus, lõpp):
    #algus = int(input("Vahemiku algus: "))
    #lõpp = int(input("Vahemiku lõpp: "))
    kokku = 0
    for i in range(algus, lõpp+1):
        kokku += i
    #print("Vahemikus olevate arvude summa on", kokku)
    return kokku

def Summeerimine_list(arvud):
    kokku = 0
    for i in range(len(arvud)):
        kokku += arvud[i]
    return kokku


##Juured // Kasuta pigem newtoni oma kui saad...
def Ruutjuur(arv):
    '''Ruutjuure leidmine arvust.'''
    uus_arv = arv ** 0.5
    return uus_arv
    
# def Ruutjuur_ast(number):
#     if float(number) < 0:
#         arvutus_viga = "Kahjuks minu programm ei oska miinusest juurt leida"
#         return arvutus_viga
#     else:
#         teisendatud_arv = round(number ** 0.5, 3)
#         return teisendatud_arv

def Ruutjuur_newton(arv):
    epsilon = 1e-09 #10**-9 #täspsuse tähistamine.
    vana_juur = 1
    uus_juur = (arv/vana_juur + vana_juur)/2
    while abs(uus_juur - vana_juur) > epsilon:
        vana_juur = uus_juur
        uus_juur = (arv/vana_juur + vana_juur)/2
    return uus_juur


## kujundid
def Pyth_hüpotenuus(a_kaatet, b_kaatet):
    '''pythagorase teoreem, c hüpotenuusi arvutamiseks'''
    return ruutjuur((a_kaatet ** 2) + (b_kaatet ** 2))

def Ringi_pindala(raadius):
    S_ring = round(3.14 * (raadius * raadius), 3)
    return S_ring

def Ringi_pikkus(raadius):
    C_ring = round(2 * 3.14 * raadius, 3)
    return C_ring
    
def Lõigu_pikkus(x1, y1, x2, y2):
    #teen vektorite kaudu
    vektor_x = abs((x2 - x1))**2
    vektor_y = abs((y2 - y1))**2
    vektor_xy = vektor_x + vektor_y
    vektor_pikkus = ruutjuur(vektor_xy)
    return vektor_pikkus


##arvuti täpsus
def Arvuti_koma_täpsus():
    '''Sellega saab arvutada arvuti koma koha täpsust.'''
    eps = 1.0 
    while eps + 1 > 1:
        eps /= 2
    eps *= 2
    print("Arvuti epsilon on:", eps)


##aeg
def Min_teis(arv):
    '''Saad minutid arvutamiseks ümber teisendada'''
    arv_uus = arv * 100 / 60
    return arv_uus

def Min_tagasi_teis(arv):
    '''Saad minutid tagasi teisendada'''
    arv_uus = arv * 60 / 100
    return arv_uus

def Tund_min(arv):
    '''Saad tunnid minutiteks teisendada'''
    arv_uus = arv * 60
    return arv_uus

def Min_tund(arv):
    '''Saad minutid tundideks teisendada'''
    arv_uus = arv / 60
    return arv_uus  


#Logaritmid
def Log(x, alus=10):
    arv_uus = Ln(x) / Ln(alus)
    return arv_uus

def Ln(x):
    n = 100000.0
    return n * ((x ** (1/n)) - 1)


##paaris paaritu
def Paaris_paaritu(arv):
    if not arv % 2:            #if arv % 2 == 0: teeb sama asja
        vastus = 'paaris'
    else:
        vastus = 'paaritu'
    return vastus

##jagatuvus
def Jagatavus(arv1, arv2):
    vastus = ''
    if arv1 > arv2:
        jagatavus = not bool(arv1 % arv2)
        if jagatavus == True:
            vastus = 'arv1 jagub arv2'
        else:
            vastus += 'arv1 ei jagu arv2'
            
    elif arv2 > arv1:
        jagatavus = not bool(arv2 % arv1)
        if jagatavus == True:
            vastus = 'arv2 jagub arv1'
        else:
            vastus += 'arv2 ei jagu arv1'
    elif arv1 == arv2:
        vastus = 'Arvud samad, jaguvad'
    return vastus