nimi = str(input('Sisestage oma nimi: '))
lubatudkiirus = int(input("Sisestage lubatud kiirus km/h: "))
tegelikkiirus = int(input("Sisestage tegelik kiirus km/h: "))
vastus = (tegelikkiirus - lubatudkiirus) * 3
miinimum = min(190, vastus)
print(str(nimi) + ", kiiruse ületamise eest on teie trahv " + str(miinimum) + " eurot.")