# Ülesanne nr. 1
# Sisesta arv ja kontrolli, kas on tegemist paarisarvu või paaritu arvuga.
# Kuidas kontrollida, kas arv on paaris või paaritu?
while True:
    try:
        arv = int(input('arv: '))

        if not arv % 2:            #if arv % 2 == 0: teeb sama asja
            print('paaris')
            break
        else:
            print('paaritu')
            break
    except ValueError:
        print('Siisesta täisarv!')
        continue
exit()