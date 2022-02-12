def xd(arv):
    return arv % 3


m = 1
while m < 60 and m != 4:
    print(xd(xd(m) + xd(m+1))) 
    m += 3 
