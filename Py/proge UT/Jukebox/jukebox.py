faili_nimi = input('Palun sisestage failinimi: ')

#Nimede listi panek

read_failist = open(faili_nimi, encoding='UTF-8')

read = []

for rida in read_failist:
    
    read.append(rida.strip('\n'))

read_failist.close()


#Laulule j2rk nr panemine

i = 0

for i in range(0,len(read),1):
    print(str(i + 1) + '. ' + str(read[i]))


#mites laul valiti

mitmes_laul = int(input('Valige laulu järjekorranumber: '))

indeksist_laulu_nr = mitmes_laul - 1

mitmes_laul_valiti = read[indeksist_laulu_nr]

print('Mängitava muusikapala on ' + str(mitmes_laul_valiti))