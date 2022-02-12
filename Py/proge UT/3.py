ruut = int(input('sisestage täisarv: '))
i = 1
suvalinelic = 1
while i < ruut:
    suvalinelic += 2**i / 2
    i += 1
print('Nisuteri ' +  str(ruut) + '. ruudu eest: ' + str(round(suvalinelic)))