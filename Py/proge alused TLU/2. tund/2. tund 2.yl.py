import math
# Ülesanne 2 Inimese kehaanalüüs
# Uurime inimest. Tundide tabelis on link valemitele, mille abil saab leida inimese ideaalkaalu, rasvaprotsendi, tiheduse, ruumala ja pindala.
# Milliseid algandmed oma arvutusteks vajad? Algandmed sisestab kasutaja.
# math.log10(x) või math.log(x, 10)


sugu = input('Mis on teie sugu?: ')
pikkus = float(input('Mis on teie pikkus sentimeetrites?: '))
kaal = float(input('Palju te kaalute kilogrammides?: '))
vanus = int(input('Kui vana te olete?: '))

if sugu == 'mees' or sugu == 'm':
    ideaalkaal_m = (3 * pikkus - 450 + vanus) * 0.25 + 45
    rasva_protsent_m = (kaal - ideaalkaal_m) / kaal * 100 + 15
    tihedus_m = 8.9 * rasva_protsent_m + (11*(100-rasva_protsent_m))
    ruumala_m = kaal / tihedus_m
    pindala_m = ((1000 * kaal) ** ((35.75 - math.log(kaal, 10)) / 53.2)) * ((pikkus ** 0.3) / 3118.2)
    print('Teie ideaal kaal on {0:}kg, teie rasva % on {1:0.3f}, tihedus {2:0.2f} kg/m^2, ruumala {3:0.3f} m^3 ning pindala on {4:0.3f} m^2'.format(ideaalkaal_m, rasva_protsent_m, tihedus_m, ruumala_m, pindala_m))
    
elif sugu == 'naine' or sugu == 'n':
    ideaalkaal_n = (3 * pikkus - 450 + vanus) * 0.225 + 40.5
    rasva_protsent_n = (kaal - ideaalkaal_n)/kaal *100 +22
    tihedus_n = 8.9 *rasva_protsent_n + (11*(100-rasva_protsent_n))
    ruumala_n = kaal / tihedus_n
    pindala_n = ((1000 * kaal) ** ((35.75 - math.log(kaal, 10)) / 53.2)) * ((pikkus ** 0.3) / 3118.2)
    print('Teie ideaal kaal on {0:}kg, teie rasva % on {1:0.2f}, tihedus {2:0.2f} kg/m^2, ruumala {3:0.3f} m^3 ning pindala on {4:0.3f} m^2'.format(ideaalkaal_n, rasva_protsent_n, tihedus_n, ruumala_n, pindala_n))
    
else:
    pass

