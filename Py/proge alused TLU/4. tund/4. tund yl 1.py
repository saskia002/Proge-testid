# Andmeteks on üliõpilaste kontrolltöö punktid ja töö maksimaalsed punktid (kõigil ühesugune).
# Hindamisel kehtivad protsentides väljendatud piirid: 
# A: 91%-100%, B: 81%-90%, C: 71%-80% jne. 
# Pane igale tööle hinne.
# Loendada, mitu õpilast said töö eest hindeks B.
# Punktid sisestab kasutaja ja peale iga sisestust küsib programm, kas on veel hindamata töid.
# Lahendust saab laiendada nii, et loendatakse iga hinde esinemine, lõpuks tehakse kokkuvõte.


punktid_tabelis = []
i = 1

while i > 0:
    if i > 0:
        punktid = float(input('Sisestage õpilase punktid: '))
        punktid_tabelis.append(punktid)
        edasi = str(input('Kas teil on veel hindamata töid? (y/n): '))
        if edasi == 'y':
            continue
        else:
            i -= 1
    else:
        i -= 1

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0

# sorteeritud_punktid_tabelid = [A, B, C, D, E, F]

for read in punktid_tabelis:
    if read >= 91 and read <= 100:
        print(str(read) + ' on hinne A')
        A += 1    
    elif read >= 81 and read < 91:
        print(str(read) + ' on hinne B')
        B += 1
    elif read >= 71 and read < 81:
        print(str(read) + ' on hinne C')
        C += 1
    elif read >= 61 and read < 71:
        print(str(read) + ' on hinne D')
        D += 1
    elif read >= 50 and read < 61:
        print(str(read) + ' on hinne E')
        E += 1
    elif read < 50:
        print(str(read) + ' on hinne F')
        F += 1 
    else:
        print('Töö punktid ei saa olla üle 100!')
        
print('Hinde A sai ' + str(A) + ' õpilast.')
print('Hinde B sai ' + str(B) + ' õpilast.')
print('Hinde C sai ' + str(C) + ' õpilast.')
print('Hinde D sai ' + str(D) + ' õpilast.')
print('Hinde E sai ' + str(E) + ' õpilast.')
print('Hinde F sai ' + str(F) + ' õpilast.')

