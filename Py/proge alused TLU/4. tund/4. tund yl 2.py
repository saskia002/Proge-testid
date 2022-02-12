import random
#random.seed()

print('Juhusliku arvu arvamis mäng. Arvuti mõtleb \njuhusliku arvu 0-10 ja sina pead selle ära arvama!\n')

game_state = True
while game_state == True:
    try:
        arvatud_kordi = 0
        pc_arv = random.randint(0, 10)
        in_arv = int(input('Arva arvu (0-10): '))
        while not pc_arv == in_arv:
            print('Arva uuesti!' + "\n")
            in_arv = int(input('Arva arvu (0-10): '))
            
            arvatud_kordi += 1
            if arvatud_kordi > 6:
                print('Oled 6x arvanud ja kaotasid arvutile!')
                m2ngu_kord = str(input('Kas soovid uuesti mängida? (y/n): '))
                if m2ngu_kord == 'y':
                    game_sate = True
                else:
                    game_state = False            
        else:
            print('Arvasid numbri ära!')
            m2ngu_kord = str(input('Kas soovid uuesti mängida? (y/n): '))
            if m2ngu_kord == 'y':
                game_sate = True
            else:
                game_state = False
                
    except(SyntaxError, ValueError):
        print('Trüki ikka arv!')
        continue
        
print('Mäng lõpetati')