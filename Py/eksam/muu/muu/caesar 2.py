# Alternatiiv: kirjuta ise programmi algusesse tähestik. Otsi krüpteeritavat tähte (str.find()) ja leia vaste tähestikust. Tähestiku piires püsimiseks on kasu jäägi leidmise tehtest (jääk tähestiku pikkusega).


tähestik = 'abcdefghijklmnopqrsšzžtuvwõäöüxy'

pikkus = len(tähestik)

cae_tekst = 'öösel sadaas vihma'
cae_samm = 9999999999578659999999999 #int(input('Sisetage samm: '))


krüptotekst = ''

#yhekaupa tähe liigutamine.
for täht in cae_tekst:
    if täht in tähestik:
        koht = tähestik.find(täht)
        uus_koht = (koht+cae_samm) % pikkus
        asendus = tähestik[uus_koht]
        krüptotekst += asendus
    else:
        krüptotekst += täht
    print(krüptotekst)
print(krüptotekst)
  
