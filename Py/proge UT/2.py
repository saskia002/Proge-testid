Suurus = float(input('Palun sisestage kirja suurus mb: '))
Pealkiri = str(input('Palun sisestage kirja pealkiri: '))
Manus = str(input('Kas kirjaga on kaasas fail? (jah), (ei): '))
ei = False
jah = True
if (float(Suurus) > 1.0 or bool(Manus)) (and bool(Pealkiri)):
    print('Kiri on spämm.')
else:
    print('Kiri ei ole spämm.')