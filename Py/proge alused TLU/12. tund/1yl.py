fail_sisse = open("tabelsis.d", "r")

tabel = list()

##py saab mitu väärtust omistada.
#esimese rea lugemine.
ridu, veerge = map(int, fail_sisse.readline().strip().split()) #map() astendamine

for rida in fail_sisse:
    int_rida = list(map(int, rida.strip().split()))
    tabel.append(int_rida)
print(tabel)
    
for r in range(ridu):
    for v in range(veerge - 2):
        if(tabel[r][v] + tabel[r][v+1] == tabel[r][v+2]):
            print(r+1, ":", v+1, " R")

for v in range(veerge):
    for r in range(ridu - 2):
        if(tabel[r][v] + tabel[r+1][v] == tabel[r+2][v]):
            print(r+1, ":", v+1, " V")

for v in range(veerge - 2):
    for r in range(ridu - 2):
        if(tabel[r][v] + tabel[r+1][v+1] == tabel[r+2][v+2]):
            print(r+1, ":", v+1, "+",r+2, ":",v+2, "=", r+3, ":", v+3, " D\n")  
        elif(tabel[r+2][v+2] + tabel[r+1][v+1] == tabel[r][v]):
            print(r+3, ":", v+3, "+",r+2, ":",v+2, "=", r+1, ":", v+1, " D\n")
        