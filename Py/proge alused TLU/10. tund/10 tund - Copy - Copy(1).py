import random
import math

def ringi_pindala(raadius):
    S_ring = round(math.pi * (raadius * raadius), 3)
    return S_ring

def ringi_pikkus(raadius):
    C_ring = round(2 * math.pi * raadius, 3)
    return C_ring

def ruutjuur_ast(number):
    if float(number) < 0:
        arvutus_viga = "Kahjuks minu programm ei oska miinusest juurt leida"
        return arvutus_viga
    else:
        teisendatud_arv = round(number ** 0.5, 3)
        return teisendatud_arv
    
def lõigu_pikkus(x1, y1, x2, y2):
    #teen vektorite kaudu
    vektor_x = abs((x2 - x1))**2
    vektor_y = abs((y2 - y1))**2
    vektor_xy = vektor_x + vektor_y
    vektor_pikkus = ruutjuur(vektor_xy)
    return vektor_pikkus

def ruutjuur_newton(arv):
    epsilon = 1e-09 #täspsuse tähistamine.
    vana_RJ = 1.0
    uus_RJ = (arv/vana_RJ + vana_RJ)/2
    while abs(uus_RJ - vana_RJ) > epsilon:
        vana_RJ = uus_RJ
        uus_RJ = (arv/vana_RJ + vana_RJ)/2
    return uus_RJ

