# """ Leia summa arvudele mingist etteantud vahemikust. Kasutaja sisestab vahemiku """
# """ alguse ja lõpu. Programm annab vastuseks soovitud vahemikku jäävate arvude summa. """
# """ Sisuliselt tegime selle ülesande läbi eelmisel nädalal while-tsükliga. Nüüd on kord for-tsükli käes. """


print('Sisetage arvude vahemik: \n')
arv1 = int(input('Sisestage vahemiku algus: '))
arv2 = int(input('Sisestage vahemiku lõpp: '))

i = 0
vahemiku_summa = 0
for i in range(arv2-arv1):
    if arv1 < i and arv2 > i:
        arv_liita = (arv1 + i)
        vahemiku_summa += arv_liita +1
        i += 1

print('Vahemiku summa on ' + str(vahemiku_summa))