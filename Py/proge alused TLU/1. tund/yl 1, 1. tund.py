print('Ül 1, värvikulu arvutamine\n')


ühiku_valik = input('Kas teie mõõtmed on sentimeetrites või meetrites?: ')

if ühiku_valik == 'meetrites' or ühiku_valik == 'm':
    a = float(input('põranda pikkus meetrites: '))
    b = float(input('põranda laius meetrites: '))
    c = float(input('Värvikulu m^2 kohta: '))
else:
    a = float(input('põranda pikkus sentimeetrites: '))
    b = float(input('põranda laius sentimeetrites: '))
    c = float(input('Värvikulu cm^2 kohta: '))

põranda_pindala = a * b

värvi_kulu = põranda_pindala * c

print('Väriv kulub ' + str(round(värvi_kulu, 2)) + ' liitrit')