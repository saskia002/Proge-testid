#ringid = int(input('Sisestage ringide arv: '))
#
#porgandid = 0
#i = 0
#
#for mitu_paaris_ringi_on in range(ringid):
#    if mitu_paaris_ringi_on % 2 == 0:
#        i += 1
#        porgandid += 2
#        
#if ringid%2 != 0:
#    porgandid -= 2
#        
#porgandid2 = porgandid * i
#
#print('Porgandite koguarv on ' + str(porgandid2) + ".")


fail = open("rebased.txt", encoding="UTF-8")

aasta = int(input('Palun sisestage, millise aasta andmeid vajate: '))

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()

for j in range(len(vastuvõetud)):
    if j + 2011 == aasta:
        print(str(aasta) + '. aastal oli vastuvõetuid ' + str(vastuvõetud[j]))
    