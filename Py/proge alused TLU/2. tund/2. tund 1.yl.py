# Ülesanne 1 Bussireis
# Lähteandmeteks on bussi väljumisaeg ja saabumisaeg. Leida bussisõidu kestvus.
# Võid eeldada, et kogu reis mahub ühe ööpäeva sisse. Vastus anna tundides ja minutites.
## väljub 12.30
##saabub 14.50

väljumis_tund = int(input('Väljumise tund: '))
väljumis_min = int(input('Väljumise minut: '))

saabumis_tund = int(input('Saabumise tund: '))
saabumis_min = int(input('Saabumise minut: '))


väljumis_min_t = väljumis_min * 100 / 60
saabumis_min_t = saabumis_min * 100 / 60

# 60 min = 100
# x min = y

palju_tunde = saabumis_tund - väljumis_tund

palju_minuteid = saabumis_min_t - väljumis_min_t

if palju_minuteid < 0:
    palju_tunde -= 1
    palju_minuteid = 100 + palju_minuteid

palju_min = palju_minuteid * 60 / 100

print('Kogu reisi pikkus oli ' + str(palju_tunde) + ' tundi ja {0:-0.0f} minutit.'.format(palju_min))