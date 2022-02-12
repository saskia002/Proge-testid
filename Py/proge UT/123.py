file = (open('rebased.txt', encoding='UTF-8'))

num = []

i = 0

for rida in file:
    num.append(rida.strip('\n'))
file.close()   

while i < len(num):
    if float(num[i]) > 0.0:
        print(float(num[i]))
    i += 1

