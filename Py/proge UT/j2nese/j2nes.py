ringid = int(input('Sisestage ringide arv: '))
porgandid = 0
i = 0

for i in range(ringid + 1):
    if i % 2 == 0:
        porgandid += i
    i += 1    
print('Porgandite koguarv on ' + str(porgandid) + ".")