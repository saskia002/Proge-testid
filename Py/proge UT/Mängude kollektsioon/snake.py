import pygame, sys, random
from pygame import Vector2

#ussi loomine
class USS:
    def __init__(self):
        self.keha = [Vector2(5, 10), Vector2(4, 10), Vector2(5, 10)]
        self.suund = Vector2(0, 0)
        self.uus_pikkus = False
           
    def ussi_loomine(self):
        for osa in self.keha:
            osa_ruut = pygame.Rect(int(osa.x * ruudu_suurus), int(osa.y * ruudu_suurus), ruudu_suurus, ruudu_suurus)
            pygame.draw.rect(raam, (183, 111, 122), osa_ruut)
            
    def ussi_liigutamine(self):
        if self.uus_pikkus == True:
            keha_kloon = self.keha[:]
            keha_kloon.insert(0, keha_kloon[0] + self.suund)
            self.keha = keha_kloon [:]
            self.uus_pikkus = False
        else:
            keha_kloon = self.keha[:-1]
            keha_kloon.insert(0, keha_kloon[0] + self.suund)
            self.keha = keha_kloon [:]
            
    def pikkuse_lisamine(self):
        self.uus_pikkus = True
    
    def reset(self):
        self.keha = [Vector2(5, 10), Vector2(4, 10), Vector2(5, 10)]
        self.suund = Vector2(0, 0)
        
#ussile 6unte loomine
class OUN:
    def __init__(self):
        self.rand()
        
    def ouna_loomine(self):
        oun_ruut = pygame.Rect(int(self.pos.x * ruudu_suurus), int(self.pos.y * ruudu_suurus), ruudu_suurus, ruudu_suurus)
        raam.blit(õun, oun_ruut)
        #pygame.draw.rect(raam, (126, 166, 114), oun_ruut)
    
    def rand(self):
        self.x = random.randint(0, ruudu_number - 1)
        self.y = random.randint(0, ruudu_number - 1)
        self.pos = Vector2(self.x, self.y)
        
#m2ngu loogika
class MAIN:
    def __init__(self):
        self.uss = USS()
        self.oun = OUN()
        
    def update(self):
        self.uss.ussi_liigutamine()
        self.kas_6un_s66di()
        self.viga()
    
    def joonistamine(self):
        self.muru_joonistamine()
        self.oun.ouna_loomine()
        self.uss.ussi_loomine()
        self.skoori_joonistamine()
        
    def kas_6un_s66di(self):
        if self.oun.pos == self.uss.keha[0]:
            # 6unale uus asukoht
            self.oun.rand()
            #ussi pikkusele lisamine
            self.uss.pikkuse_lisamine()
        # 6una ussi keha sisse spawnimise 2ra hoidmine
        for ruut in self.uss.keha[1:]:
            if ruut == self.oun.pos:
                self.oun.rand()
    
    def viga(self):
        #kas uss puutus seinu 
        if not 0 <= self.uss.keha[0].x < ruudu_number or not 0 <= self.uss.keha[0].y < ruudu_number:
            self.game_over()
        #v6i ise enda saba
        for ruut in self.uss.keha[1:]:
            if ruut == self.uss.keha[0]:
                self.game_over()
            
    def game_over(self):
        self.uss.reset()
        
    def muru_joonistamine(self):
        muru_v2rv = (167, 209, 61)
        for rida in range(ruudu_number):
            if rida % 2 == 0:
                for veerg in range(ruudu_number):
                   if veerg % 2 == 0:
                        muru_ruut = pygame.Rect(veerg * ruudu_suurus, rida * ruudu_suurus, ruudu_suurus, ruudu_suurus)
                        pygame.draw.rect(raam, muru_v2rv, muru_ruut)
            else:
                for veerg in range(ruudu_number):
                   if veerg % 2 != 0:
                        muru_ruut = pygame.Rect(veerg * ruudu_suurus, rida * ruudu_suurus, ruudu_suurus, ruudu_suurus)
                        pygame.draw.rect(raam, muru_v2rv, muru_ruut)
                        
    def skoori_joonistamine(self):
        skoori_text = str(len(self.uss.keha) - 3)
        skoori_n2itamine = m2ngu_font.render(skoori_text, True, (56, 74, 12))
        skoor_x = int(ruudu_suurus * ruudu_number - 60)
        skoor_y = int(ruudu_suurus * ruudu_number - 40)
        skoor_ruut = skoori_n2itamine.get_rect(center = (skoor_x, skoor_y))
        õun_ruut = õun.get_rect(midright = (skoor_ruut.left, skoor_ruut.centery))
        taust_skoor = pygame.Rect(õun_ruut.left, õun_ruut.top, õun_ruut.width + skoor_ruut.width + 6, õun_ruut.height)
        
        pygame.draw.rect(raam, (164, 209, 61), taust_skoor)
        raam.blit(skoori_n2itamine, skoor_ruut)
        raam.blit(õun, õun_ruut)
        pygame.draw.rect(raam, (56, 74, 12), taust_skoor, 2)

#raam
pygame.init()
pygame.display.set_caption('Snake')
ruudu_suurus = 40
ruudu_number = 20
raam = pygame.display.set_mode((ruudu_number * ruudu_suurus, ruudu_number * ruudu_suurus))

#grafika ja font
õun = pygame.image.load('graafika/oun.png').convert_alpha()
m2ngu_font = pygame.font.Font(None, 25)

#timer ja max fps
clock = pygame.time.Clock()
ekraani_v2rskendus = pygame.USEREVENT
pygame.time.set_timer(ekraani_v2rskendus, 150)

#main loop
main_m2ng = MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #l6petab k6ik koodi
        if event.type == ekraani_v2rskendus:
            main_m2ng.update()
        #klaviatuuriga ussi suuna muutmine
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_m2ng.uss.suund.y != 1:
                    main_m2ng.uss.suund = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_m2ng.uss.suund.y != -1:
                    main_m2ng.uss.suund = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_m2ng.uss.suund.x != -1:
                    main_m2ng.uss.suund = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_m2ng.uss.suund.x != 1:
                    main_m2ng.uss.suund = Vector2(-1, 0)
    raam.fill((175, 215, 70))
    main_m2ng.joonistamine()
    pygame.display.update()
    clock.tick(60) #max fps 60