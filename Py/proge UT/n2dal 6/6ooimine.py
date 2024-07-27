rahvas = int(input("Sisestage kylaliste arv: "))

def tervitus(x):
    print('Võõrustaja: "Tere!"')
    print('Täna ' + str(x) + '. kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')
a = 0        
for a in range(rahvas):
    tervitus(a + 1)