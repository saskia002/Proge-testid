global a # pea programi muutuja....


esimene(c, d):
    print("esimene: c", c)
    print("esimene: d", d)
# Mis juhtub, kui:
#     a = 4
#     b = 6
    print("esimene: a", a)
    print("esimene: b", b)
#    print("esimene: e", e)
#    print("esimene: f", f)
# Kuidas (ja kas) muutub olukord, kui funktsioon teine() hoopis siin vÃ¤lja kutsuda?
#    teine(c,d)

def teine(e, f):
    print("teine: e", e)
    print("teine: f", f)
    print("teine: a", a)
    print("teine: b", b)
#    print("teine: c", c)
#    print("teine: d", d)

a = 3
b = 5
esimene(a, b)
#teine(a, b)

print("peaprog: a", a)
print("peaprog: b", b)