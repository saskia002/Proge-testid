#kood 210783
def yl_leidmine(num):
    jääk_arvutus = (num % 6) + 1
    return jääk_arvutus
##sain yl 4.

#0. pealkiri ja sisestus.
print("Programm nende päevade keskmise temperatuuri leidmiseks,\nkus kraadiklaas näitas külmakraade.\n")
faili_nimi = str(input("Sisestage faili nimi: "))

# 1. loen failist.
list_päev = []
list_temp = []
fail = open(faili_nimi)
for rida2 in fail:
    #päevad ja temp
    if rida2[2] == " ":
        list_päev.append(int(rida2[0:2]))
        list_temp.append(int(rida2[3: len(rida2)-1]))
    elif rida2[1] == " ":
        list_päev.append(int(rida2[0:1]))
        list_temp.append(int(rida2[2: len(rida2)-1]))       
fail.close()

#2. keskmise temp arvutamine.
päevi_kuus = list_päev[-1]
arv_kokku = 0
i = 0
j = 0
while i < päevi_kuus:
    if list_temp[i] < 0:
        arv_kokku += list_temp[i]
        j += 1
    i += 1
arv_kokku = round(arv_kokku / j, 2)

#3. Väljastus...
if j == 0:
    print("Ühtelgi päeval polnud miinus kraade! :)")
else: 
    print("{0:}. päeval oli miinus kraadid.\nPäeva keskmine temp. oli {1:}!  ".format(j, arv_kokku))




    

    
    