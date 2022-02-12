# NÃ¤ide listi elementide lÃ¤bimisest
# KÃµigepealt luuakse list sisestatud nimedest
# ja seejÃ¤rel trÃ¼kitakse kÃµik nimed vÃ¤lja

nimed = list()                 # Teeme tÃ¼hja listi
mitu = int(input("Mitu nime varuks on? "))
for i in range(mitu):      # TsÃ¼kkel tÃ¶Ã¶tab "mitu" korda.
    uus_nimi = input("TrÃ¼ki nimi ")
    nimed.append(uus_nimi)

# Massiivi saab ka tervikuna vÃ¤lja trÃ¼kkida, aga see ei nÃ¤e vÃ¤lja ilus
# ja on pigem kasutatav kontrollvÃ¤ljatrÃ¼kina.
print(nimed)

# Nimed vÃµetakse listist Pythonile omasel nÃ¶ foreach-tÃ¼Ã¼pi tsÃ¼kli kujul

for nimi in nimed:
    print(nimi)
print("Sisestasid", len(nimed), "nime.")  # Funktsioon len() tagastab listi pikkuse
print("TÃ¤nan tÃ¤helepanu eest!")

# for i in range(a, b, c)
# a - algus
# b mis list
# c - samm