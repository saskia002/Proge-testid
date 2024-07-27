#1. argument, millega arvutab v2lja metsa juurde kasvu ja ymardab o.o1

def juurdekasv(metsa_pindala_aakrites, aastane_juurdekasv):
    metsa_juurdekasv = metsa_pindala_aakrites * 0.4047 * aastane_juurdekasv
    return round(metsa_juurdekasv, 2)

#2. kysib faili nime ja juurdekasvu ning millest suuremaid arvesse v6tta
ff = input('Sisestage failinimi: ')
juurde_aastas = float(input('Sisestage aastane juurdekasv hektari kohta tihumeetrites: '))
maks_suurus = float(input('Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võetakse: '))


#3. failist lugemine ja loendisse panek
metsa_suurus_failis = []
f = open(ff)
for rida in f:
    metsa_suurus_failis += [float(rida)]

#4. numrite v6rdlemine ja argumendi kasutamine.
#4. kui see v2iksem kui sisestaud maks suurus siis error
#5. mitu metsa l2ks sellega kokku mis maks olid

mitu_loeti = 0

for xd in metsa_suurus_failis:
    if xd > maks_suurus:
        print('Metsatüki aastane juurdekasv on ' + str(juurdekasv(xd, juurde_aastas)))
        mitu_loeti += 1
    else:
        print('Metsatükki ei võeta arvesse')
        
print('Arvutati ' + str(mitu_loeti) + ' metsatüki juurdekasv.')
        
        
        
        
        
        