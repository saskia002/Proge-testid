import random
import math

def Ringi_pindala(raadius):
    S_ring = round(math.pi * (raadius * raadius), 3)
    return S_ring

def Ringi_pikkus(raadius):
    C_ring = round(2 * math.pi * raadius, 3)
    return C_ring

def Ruutjuur_ast(number):
    if float(number) < 0:
        arvutus_viga = "Kahjuks minu programm ei oska miinusest juurt leida"
        return arvutus_viga
    else:
        teisendatud_arv = round(number ** 0.5, 3)
        return teisendatud_arv
    
def Lõigu_pikkus(x1, y1, x2, y2):
    #teen vektorite kaudu
    vektor_x = abs((x2 - x1))**2
    vektor_y = abs((y2 - y1))**2
    vektor_xy = vektor_x + vektor_y
    vektor_pikkus = ruutjuur(vektor_xy)
    return vektor_pikkus

def Ruutjuur_newton(number):
    epsilon = 1e-09 #10**-9 #täspsuse tähistamine.
    vana_juur = 1
    uus_juur = (number/vana_juur + vana_juur)/2
    while abs(uus_juur - vana_juur) > epsilon:
        vana_juur = uus_juur
        uus_juur = (number/vana_juur + vana_juur)/2
    return uus_juur
 

arvud = 0
arvud_max = 20
while arvud < 20:
    arv_arvuti = random.randint(arvud, arvud_max)
    arv_ruutjuur = Ruutjuur_newton(arv_arvuti)
    arv_sqrt_math = math.sqrt(arv_arvuti)
    print("Arvuti: {0:}\nMina: {1:}\nPyMath: {2:}\n".format(arv_arvuti, arv_ruutjuur, arv_sqrt_math))
    arvud += 1
    
    
    