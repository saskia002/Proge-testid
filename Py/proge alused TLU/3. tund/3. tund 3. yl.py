# Ülesanne nr 3 Kolmnurga kontroll
# Joosepil on kolm kaigast. Kas nendest saab moodustada kolmnurga? Otsustamiseks vajame 
# kaigaste pikkuseid, mida tuleb Joosepilt küsida (ehk programmis sisestada).

# a + b > c

külg1 = float(input('1. külje pikkus: ')) #a
külg2 = float(input('2. külje pikkus: ')) #b
külg3 = float(input('3. külje pikkus: ')) #c


if külg1 + külg2 > külg3 and külg2 + külg3 > külg1 and külg3 + külg1 > külg2:
#     if külg1 + külg2 > külg3:
#     
#         if külg2 + külg3 > külg1:
#             if külg3 + külg1 > külg2:
    print('peaks saama kyll')  
else:
    print('Kolmnurka pole võimalik koostada.')