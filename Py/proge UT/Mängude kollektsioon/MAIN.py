from easygui import *
import sys

msgbox('Mängude kollektsioon \nSiim xddddddd')
nupud = ['Kivi/Paber/käärid', 'Snake', 'Quit']
vajutati = buttonbox("Palun valige mäng mida soovite mängida:  ", choices = nupud)

if vajutati == 'Kivi/Paber/käärid':
    import kpk
elif vajutati == 'Snake':
    import snake
else:
    sys.exit()