# Ülesanne 1 Väikesed näpuharjutused meetodeid kasutades
# a) Sisestatakse tekstilõik ja otsitav sõna. Programm leiab, kas tekstilõigus on olemas otsitav sõna
# ja annab vastuseks, "Sõna ei leidnud" või "Sõna algas ... positsioonist".
# b) Sisestatakse tekstilõik, otsitav sõna ja asendussõna. Programm uurib, kas otsitav sõna on olemas. Kui jah,
# siis asendab selle sõna asendussõnaga ja trükib teksti uuesti välja, vastasel juhul annab teate, et otsitavat 
# sõna ei leitud ja asendamist ei toimu.
# Abiks on meetodid str.find(), str.replace().

text_par = 'maali maasikas one nibaa'
text_find = 'one'
text_replace = 'big'

if text_find in text_par: #kui see sõna on lauses, siis
    print(text_par.replace(text_find, text_replace, text_par.find(text_find)))
else:
    print('''uups sõna puudub tekstist :'(''')