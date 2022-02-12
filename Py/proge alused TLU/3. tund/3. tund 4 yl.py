# Ülesanne nr. 4 Ruutvõrrand
# ax^2 + bx + c = 0 on ruutvõrrand. Kirjutada programm, mis laseks sisestada
# ruutvõrrandi kordajad (a, b, c) ja leiaks väärtused x1-le ja x2-le ehk 
# ruutvõrrandi reaalarvulised lahendid.
# Arvestada tuleb kindlasti sellega, et alati ei ole ruutvõrrandil reaalarvulisi 
# lahendeid. Kui aga ruutliikme kordajaks sisestada 0, siis ei ole üldse ruutvõrrand.
# 
# Selles ülesandes on lubatud vahelduseks kasutada muutujaid a, b, c ;)
# 
# Testandmed antud ülesande jaoks:
# a       b       c       x1      x2
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# 2       5       2      -0.5     -2
# 3       2       -1      0.33    -1
# 2       2       2       reaalarvulised lahendid puuduvad
# 2       4       2       -1
# 
# --------------------------------------------------
# 
# Räägime vahepeal positsioonilistest arvusüsteemidest, täpsemalt kahend-, kahksand- ja 
# kuueteistkümnendsüsteemist.
# Harjutamiseks tuleb järgnevad arvud teisendada 2nd, 8nd ja 16ndsüsteemi ja uuesti tagasi
# kümnendsüsteemi. 
# 58
# 128 
# 19


print('Ruutvõrrand ax^2 + bx + c = 0 lahendamine\n')

a = float(input('Sisestage a väärtus: '))
b = float(input('Sisestage b väärtus: '))
c = float(input('Sisestage c väärtus: '))


#kala on sees.

x_1 = (-(b) + (((b**2) - (4*a*c))**0.5)) / 2*a
x_2 = (-(b) - (((b**2) - (4*a*c))**0.5)) / 2*a




