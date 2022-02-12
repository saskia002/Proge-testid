# Ülesanne 2 Caesari salakiri
# Salakirjad on olnud populaarsed aastatuhandeid. Üks lihtsamaid nendest on nn Caesari salakiri. Selle põhimõte on lihtne:
# lepitakse kokku samm, mille kauguselt tähestikust võetakse sõnas oleva tähe asemele asendustäht. Sama sammu /nihet kasutatakse
# iga tähe jaoks. Näiteks sõna "kala" krüpteeruks sammu 4 korral "oepe". Kui samm läheb üle tähestiku lõpu, jätkatakse 
# liikumist algusest. Teise kirjelduse (Wikipedia) järgi tehakse nihe vasakule - siis saaks sõnast "kala" "gwhw
# Programmi ülesanne on küsida sõna (või ka lause), küsida samuti nihe/samm ja krüpeerida sõna antud sammuga. Olukorra lihtsustamiseks eeldame, et tekstis on vaid ladina tähed. Samas peab aga jälgima, et kirjavahemärgid tühikud jms paika jääksid.
# 
# Kasulikeks funktsioonideks osutuvad siin: 
# ord() - annab ASCII-tabeli alusel tähe koodi ja
# chr() - tuletab koodist sümboli (ikka ASCII tabeli alusel)
# Töö käik: leia kood, liida samm, leia täht (sümbol)
# Tööd tuleb teha stringis täht haaval for-tsükliga. Probleem tekib siis, kui kood läheb suuremaks kui tähestikus viimasel tähel. Kuidas jõuda tagasi tähestiku piiridesse?
# 
# Alternatiiv: kirjuta ise programmi algusesse tähestik. Otsi krüpteeritavat tähte (str.find()) ja leia vaste tähestikust. Tähestiku piires püsimiseks on kasu jäägi leidmise tehtest (jääk tähestiku pikkusega).

cae_tekst = 'kala'
cae_samm = 4 #int(input('Sisetage samm: '))


krüptotekst = ''

#yhekaupa tähe liigutamine.
for täht in cae_tekst:
    #tähenihutamine.
    ##print(täht, ord(täht), ord(täht)+cae_samm, chr(ord(täht)+cae_samm))
    krüptotekst += chr(ord(täht)+cae_samm)
    print(krüptotekst)
    
print(krüptotekst)