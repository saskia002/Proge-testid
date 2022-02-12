# # muutujale antakse komakohaga väärtus, seejärel trükitakse see välja
# # täpsusega kolm kohta peale koma
# 
# arv = 13.45685343634636
# 
# # Nn old-style formatting
# print("Arv %f on kolme komakohani ümardatult %0.3f." % (arv,arv))
# 
# # Nn new-style formatting
# print("Arv {0:f} on kolme komakohani ümardatult {0:0.3f}.".format(arv))
# 
# 
# print(round(arv,3))


#// d - decimal | %10.2f - välja laius , .2f on kaks kohta pleae koma, kymme tyhikut | %10d

# # # Muutujatele antakse väärtus ja trükitakse see välja
# # # On määratud komakohtade arv ja trükivälja laius.
# # # Kriipsud on teises reas selleks, et saaksid paremini tühikuid lugeda
# # # ja püüda sel viisil trükivälja laiuse määramise põhimõttest aru saada.
# # # Mõlemas formaadis on välja laiuseks 10 kohta.
# # arv_i = 5
# # arv_f = 6.0
# # # Nn old-style formatting
# # print("%10.2f %10d" % (arv_f, arv_i**2))
# # print("----------------------")
# # 
# # # Nn new-style formatting
# # print("{0:10.2f} {1:10d}".format(arv_f, arv_i**2))
# # print("----------------------")



# # # # Nime (stringitüüpi väärtus, mida ei ole vaja teisendada) küsimine ja väljatrükk
# # # # Sellise print-lausega on tülikas tühikuid päris korda saada.
# # # 
# # # minu_nimi = input("Mis su nimi on?: ")
# # # print("Tere", minu_nimi, ". Lahe nimi sul. Sinuga oli tore tutvuda!")
# # # print("Tere ", minu_nimi, ". Lahe nimi sul. Sinuga oli tore tutvuda!", sep='£') #sep='' koma koha pleale kirjutatud koma eelmaldamine, separation.
# # # 
# # # # Võrdle väljatrükke ja mõtle tühikute korrektsusele.
# # # # Parameeter sep=... määrab, milline sümbol trükitakse koma kohale ehk
# # # # väljatrükis erinevate osade vahele. Vaikimisi on selleks sümboliks tühik.

# 
# print('dssdfs', end='') #// end='' - reavahetus l6ppeb sellega millega rida lõpeb.

# // - täis arv jagamine
# % - jäägi leidmine


