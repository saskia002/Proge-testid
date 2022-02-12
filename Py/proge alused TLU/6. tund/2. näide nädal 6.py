mitu = int(input("Mitu inimest? "))
pikkused = list()
nimed = list()
for i in range(mitu):
    nimi = input("Nimi ")
    nimed.append(nimi)
    pikkus = int(input("Pikkus "))
    pikkused.append(pikkus)


for i in range(len(nimed)):
    print("Nimi:",nimed[i],"ja pikkus", pikkused[i])


keskmine = 0
for i in range(len(pikkused)):
    keskmine += pikkused[i]
keskmine /= len(pikkused)

#min arvud listis
# võrdlen ühe kaupa ja suurim võidab 

suurim_arv = 0
arv1 = 0
arv2 = 0
for i in range(len(pikkused)):
    arv1 = pikkused[i]
    arv2 = pikkused[len(pikkused)-1]
    i +=1
    if arv1 > arv2:
        if arv1 > suurim_arv:
            suurim_arv = arv1
    elif arv2 > arv1:
        if arv2 > suurim_arv:
            suurim_arv = arv2

# list1 = [20,1,442,123123,0]
# 
# list1.sort()
# 
# list2 = max(list1)
# 
# list3 = min(list1)