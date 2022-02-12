##dictionary pean tegema

sõnastik = dict()
# sõnastik ["a"] = 1
# tähestik = []
# tähestik = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]


#loen failist...lower()
def loe_fail(faili_nimi):
    fail = open(faili_nimi)
    for rida in fail:
        ##siia see sõnastiku lsiamine......
        rida2 = rida.lower()
        print(rida2)
        #seda on lieda sealt tunni alt kus need tupled olid....
            
#     read = fail.readlines(1)
    print(read)
    fail.close()

    
#tähestiku sõnastik...

Faili_valik = loe_fail(input("Siesta palun faili nimi mida soovi avada: "))




