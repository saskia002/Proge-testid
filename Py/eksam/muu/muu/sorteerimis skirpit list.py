# Ülesanne 2 Sorteerimine mullimeetodil
# Mullimeetod (bubble sort) töötab järgmiselt:
# alustades 1. elemendist võrreldakse kahte kõrvuti asuvat elementi ja vahetatakse nad omavahel,
# kui väiksem on tagapool. Nii toimitakse järjest kõigi kõrvuti asuvate elementidega.
# Peale esimest korda listi lõppu jõudmist on kõige suurem arv listis viimane.
# Teised on aga suure tõenäosusega segamini.
# Seega tuleb alustada uuesti algusest ja korrata sama tegevust.
# Mitu korda on sorteerimiseks vaja list läbi käia? Üle N korra (elementide arv) kindlasti
# mitte. Tegelikult võib piisata ka vähemast.
# Andmed on sorteeritud, kui kogu listi läbimise ja paaride võrdlemise jooksul
# ei ole vaja teha ühtegi vahetust. Kasuta seda korduste arvu määramiseks.
# Sorteeritav list genereeri juhuslike arvude generaatoriga.
# Tee programmist teine versioon, mis sorteeriks arvud mittekasvavasse järjekorda.

import random
mitu = 10

arvud = []

for i in range(mitu):
    arv = random.randint(0, 100)
    arvud.append(arv)
print(arvud)

# #teeb arvud massivi arvu kordi l2bi.
# for x in range(len(arvud)):
#     for i in range(mitu-1):
#         if arvud[i] > arvud[i+1]:
#             #a to c
#             vahe_arv = arvud[i]
#             #b to a
#             arvud[i] = arvud[i+1]
#             #c to b
#             arvud[i+1] = vahe_arv
# print(arvud)

# #teeb nii kaua kuni sorteeritud.
kas_on_vahetatud = True
mitu_korda_vahetati = 0

while(kas_on_vahetatud):
    kas_on_vahetatud = False
    for i in range(mitu-1):
        if arvud[i] > arvud[i+1]:  
            vahe_arv = arvud[i]
            arvud[i] = arvud[i+1]
            arvud[i+1] = vahe_arv
            kas_on_vahetatud = True
    mitu_korda_vahetati += 1
print(arvud)    