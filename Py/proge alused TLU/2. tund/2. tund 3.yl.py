# Ülesanne 3 Rahatagastaja
# ------------------------
# Ostad kaupa N euro eest.
# Vastavalt Sinu poolt makstud rahale tuleb Sulle raha tagasi anda. Milliseid rahatähti ja kui palju tuleks tagastada?
# Eeldame, et arveldatakse ainult eurodes (st sentideta).
# Programm küsib, kui palju maksab kaup ja kui palju ostja raha annab. Vastuseks trükib programm ekraanile, millises vääringus ja mitu 
# rahatähte tagasi anda tuleb.
# 
# Väljatrükk oleks midagi sellist:
# --------------------------------
# Sa maksid 500 eurot, kaup maksis 133 eurot. Saad tagasi 367 eurot:
# 0 viiesajalist
# 1 kahesajalist
# 1 sajalist
# 1 viiekümnelist
# 0 kahekümnelist
# 1 kümnelist
# 1 viielist
# 1 kahelist
# 0 ühelist
# 
# Programm võib, kuid ei pea kontrollima, kas maksti õige summa raha ja võib väljastada ka (nagu näites näha) koguse 0 tükki.
# Kuid kasutades tingimuslauset, saab nimetatud probleeme vältida.



palju_maksab_kaup = int(input('Palju maksab kaup?: '))
ostja_antud_rahasumma = int(input('Palju raha ostja andis?: '))

# viiesa = []
# kahesa = []
# saja = []
# viieky = []
# kaheky = []
# ky = []
# viis = []
# kaks = []
# yks = []

if palju_maksab_kaup > ostja_antud_rahasumma:
    print('Teil pole piisavalt raha... :(')
    
elif palju_maksab_kaup <= ostja_antud_rahasumma:
    raha_tagasi = ostja_antud_rahasumma - palju_maksab_kaup
#     leiab l2bi j22kide




