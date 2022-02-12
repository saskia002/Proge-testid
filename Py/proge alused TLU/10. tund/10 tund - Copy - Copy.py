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

def ruutjuur_newton(number):
    epsilon = 1e-09 #10**-9 #täspsuse tähistamine.
    vana_juur = 1
    uus_juur = (number/vana_juur + vana_juur)/2
    while abs(uus_juur - vana_juur) > epsilon:
        vana_juur = uus_juur
        uus_juur = (number/vana_juur + vana_juur)/2
    return uus_juur

# eps = 1.0 ##sellega saab arvutada arvuti koma koha täpsust.
# while eps + 1 > 1:
#     eps /= 2
# eps *= 2
# print("The machine epsilon is:", eps)




