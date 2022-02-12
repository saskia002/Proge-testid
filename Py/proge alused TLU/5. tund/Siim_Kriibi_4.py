from random import randint

game_state = False
#algus sõnum
print('\n Arvuti numbri võrdlus mäng!\n')
while game_state == False:
        user_resume_game = input('Kas te soovite mängida? (y/n): ')
        if user_resume_game == 'y' or user_resume_game == 'Y':
            game_state = True
        elif user_resume_game == 'n' or user_resume_game == 'N':
            game_state = False
            print('\nAitäh, et ei mänginud minu ägedat mängu!\n')
            exit()
        else:
            print('\nKirjutasite programmi jaoks tundmatu vastuse! Proovige uuesti.')
            continue
#main mäng
while True:
    while game_state == True:  
        #randint gen
        random_num_1 = randint(1, 10)
        random_num_2 = randint(1, 10)
        random_num_3 = randint(1, 10)
        #Kas mõni number on sama väärtusega.
        if random_num_1 == random_num_2 == random_num_3:
            print('Kõik arvutipoolt loodud arvud on samad!')
            game_sate = False
        else: 
            if random_num_1 == random_num_2:
                print('Arv 1 ja 2 on sama väärsed!')
                game_state = False
            elif random_num_1 == random_num_3:
                print('Arv 1 ja 3 on sama väärsed!')
                game_state = False
            elif random_num_2 == random_num_3:
                print('Arv 2 ja 3 on sama väärsed!')
                game_state = False 
            else:
            #Kõige suurema numbri valimine.
                if random_num_1 > random_num_2 and random_num_1 > random_num_3:
                    print('Number 1 on kõige suurem')
                    game_state = False 
                elif random_num_2 > random_num_1 and random_num_2 > random_num_3:
                    print('Number 2 on kõige suurem')
                    game_state = False 
                elif random_num_3 > random_num_1 and random_num_3 > random_num_2:
                    print('Number 3 on kõige suurem')
                    game_state = False
            print('1. oli {0:},\n2. oli {1:},\n3. oli {2:}.'.format(random_num_1, random_num_2, random_num_3))                
    #Kontroll kas tahetakse jätkata.             
    else:
        user_resume_game = input('Kas te soovite uuesti mängida? (y/n): ')
        if user_resume_game == 'y' or user_resume_game == 'Y':
            game_state = True
        elif user_resume_game == 'n' or user_resume_game == 'N':
            game_state = False
            print('\nAitäh, et mängisid minu ägedat mängu!\n')
            exit()
        else:
            print('Kirjutasite programmi jaoks tundmatu vastuse! Proovige uuesti.')
            continue
    
