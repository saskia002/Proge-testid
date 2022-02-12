import time
kordajad1 = [1,2,3,4,5,6,7,8,9,1]
kordajad2 = [3,4,5,6,7,8,9,1,2,3]
kuud = ['', 'jan', 'veb', 'mär', 'apr', 'mai', 'jun', 'jul' ,'aug', 'sept', 'okt', 'nov' ,'dets']
ik = input('Sisestage oma IK: ')

sünniaasta = 0
sünnikuu = int(ik[3:5])
sünnipäev = int(ik[5:7])
sugu = str(ik[0])
sünnikuu_nimi = kuud[sünnikuu]

while True:
        try:
            if int(sugu) == 3 or int(sugu) == 4:
                sünniaasta = str(19)
                sünniaasta += ik[1:3]
                sünniaasta = int(sünniaasta)
            elif int(sugu) == 5 or int(sugu) == 6:
                sünniaasta = str(20)
                sünniaasta += ik[1:3]
                sünniaasta = int(sünniaasta)
            else:
                sünniaasta = str(18)
                sünniaasta += ik[1:3]
                sünniaasta = int(sünniaasta)
                
            if not int(sugu) % 2:
                sugu = 'naine'
            else:
                sugu = 'mees'
                
            i = 0
            ktr_sum = 0
            for i in range(len(kordajad1)):
                ktr_sum += int(ik[i]) * kordajad1[i]
                i += 1
                break
            ktr_sum %= 11
            if ktr_sum == 10:
                i = 0
                ktr_sum = 0
                for i in range(len(kordajad2)):
                    ktr_sum += int(ik[i]) * kordajad2[i]
                    i += 1
                    break
                ktr_sum %= 11
                if ktr_sum == 10: 
                    ktr_sum = 0
                    
            aeg = time.localtime()
            hetke_päev = aeg[2]
            hetke_kuu = aeg[1]
            hetke_aasta = aeg[0]

            #vanuse kontoll
            vanus = 0
            #aasta #kuu #päev
            vanus = hetke_aasta - sünniaasta
            if hetke_kuu <= sünnikuu:
                if hetke_päev < sünnipäev:
                    vanus -= 1

            print('Teie olete süninud {1}.{2}.{3} ja te olete {0}. a vana.\nTe olete {4} soost ning IK kontroll number on {5}.'.format(vanus, sünnipäev, sünnikuu_nimi, sünniaasta, sugu, ktr_sum))
        except ValueError:
            print('Sellist inimest pole olemas või võimalik koostada!')
            break
    