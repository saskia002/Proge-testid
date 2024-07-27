import pygame
import sys
import random

#ussi ja toidu klassid ning raamistiku tegemine
class uss(object):
    def __init__(ei):
        ei.pikkus = 1
        ei.pos = [((500 / 2), (500 / 2))]
        ei.suund = random.choice([yles, alla, paremale, vasakule])
        ei.v2rv = (0, 0, 0)
    
    def pea_pos(ei):
        return ei.pos[0]
    
    def p66ramine(ei):
        if ei.pikkus > 1 and (point[0] * -1, point[1] * -1) == ei.suund:
            return
        else:
            ei.suund = point
            
    def liikumine(ei)
        p22 = ei.pea_pos()
        x, y = ei.suund
        uus = (((p22[0] + (x*500)) % 500), (p22[1] + (y*500)) %500)
        if len(ei.pos) > 2 and uus in ei.pos[2:]:
            ei.null()
        else:
            5.31
        
class toit(object):

def ruutustik(pind):
    for y in range(0, int(ruut_pikkus)):
        for x in range(0, int(ruut_k6rgus)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*20, y*20,), (20, 20))
                pygame.draw.rect(pind, (178, 189, 8), r)
            else:
                rr = pygame.Rect((x*20, y*20,), (20, 20))
                pygame.draw.rect(pind, (168, 179, 0), re)

#ruudustiku loomine
ruut_suurus = 20
ruut_laius = 500 / 20
ruut_k6rgus = 500 / 20

#liikumis kordinaadidi
yles = (0, -1)
alla = (0, 1)
vasakule = (-1, 0)
paremale = (1, 0)

#main loobi loomine
pygame.init()
aeg = pygame.time.Clock()
raam = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('snake')

pind = pygame.Surface(raam.get_size())
pind = pind.convert()
ruutustik(pind)

uss = uss()
toit = toit()

skoor = 0
while True
    clock.tick(10)
    screen.blit(pind, (0, 0))
    pygame.diplay.update()
