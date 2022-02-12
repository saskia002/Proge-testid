# Ülesanne nr 2 Jaguvus
# Sisestatakse 2 arvu. Kontrollitakse, kas suurem arv jagub väiksema arvuga
# ja väljastatakse sellekohane vastus. Programm peab ise aru saama, kumb arv suurem on.
# Kuidas kontrollida jaguvust?

arv1 = float(input('arv1: '))
arv2 = float(input('arv2: '))

if arv1 > arv2:
    jagatavus = not bool(arv1 % arv2)
    if jagatavus == True:
        print('arv1 jagub arv2')
    else:
        print('arv2 ei jagu arv1')
        
elif arv2 > arv1:
    jagatavus = not bool(arv2 % arv1)
    if jagatavus == True:
        print('arv2 jagub arv1')
    else:
        print('arv2 ei jagu arv1')
        
else:
    print('Kirjuta ikka numbrid mitte tähed!')
    
