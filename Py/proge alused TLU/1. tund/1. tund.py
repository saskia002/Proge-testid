from math import sqrt
# Täisnurkse kolmnurga kohta on teada tema kaatetite pikkused. Leida kolmnurga pindala. 
# Millised sammud tuleks selle jaoks läbida? Koostame lahenduse selliselt, et ta oleks suuteline leidma
# igasuguses mõõtmes täisnurksete kolmnurkade pindalasid. See tähendab, et peame andma võimaluse inimesele
# anda programmile ette erinevaid andmeid.
# Kas on võimalik lisada ka ümbermõõdu arvutamist? Kui jah, siis kuidas?

a = float(input('esimene kaatet: '))
b = float(input('teine kaatet: '))
c = sqrt((a**2) + (b**2))

S = a * b / 2
P = a + b + c 

Valik = input('Kas te soovite arvutada pindala või ümbermõõtu?\nValik: ')

if Valik == str('pindala'):
    print('Pindala on ' + str(round(S, 2)) + ' üh⌃2')
else:
    print('Ümbermõõt on ' + str(round(P, 2)) + ' üh')
