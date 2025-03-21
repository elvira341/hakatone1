import pygame as pg  # ипортируем библиотеку
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False  # согласовывыем начало координат с pygame


RES = WIDTH, HEIGHT = 1200, 650  # размер эерана
FPS = 240  # частота обновления кадра

pg.init()  # инициализация pygame
display = pg.display.set_mode(RES)  # Окно игры: размер, позиция
clock = pg.time.Clock()  # создать объект, чтобы помочь отслеживать время.
bgfon = pg.image.load('fone.jpg')
bgfon = pg.transform.scale(bgfon, (WIDTH, HEIGHT))

class Player:
    def __init__(self, mana, lives, attack2):
        self.mana = mana
        self.lives = lives
        self.attack2 = attack2
    def draw_pl(self):
        y = 0
        x = 60
        image = pg.image.load('degrass.jpg')
        display.blit(image, (int(x), int(y)))
    def attack1(self, var_vrag, var_w, ):

        for i in Wearpon_info(var_w).values():
            m = Wearpon(i['damage'])
            wearpon_d = int(m)
        for n in vrazhina_info(var_vrag).values():
            n = Vrazhina(n['lives'])
            vrag_hp = int(n)
        vrag_hp = vrag_hp - wearpon_d



player_info = {'player':{ 'mana': 100, 'lives': 60, 'attack2': 60}}

class Vrazhina:
    def __init__(self, image, mana, lives, pos, attack1, attack2):
        self.image = image
        self.mana = mana
        self.lives = lives
        self.attack1 = attack1
        self.attack2 = attack2
        self.pos = pos
    def draw(self):
        y = 0
        x = self.pos
        image = pg.transform.scale(self.image)
        display.blit(image, (int(x), int(y)))

vrazhina_info = {
     'hilichurl': {'image': 'hilichurl.jpg', 'mana': 100, 'lives': 60, 'attack1': 10, 'attack2': 15 },
     'shamachurl': {'image': 'shamachurl.jpg', 'mana': 100, 'lives': 80, 'attack1': 15, 'attack2': 20 },
     'lavachurl': {'image': 'lavachurl.jpg', 'mana': 150, 'lives': 110, 'attack1': 20, 'attack2': 35 },
}

class Wearpon:
    def __init__(self, image, damage, mana_sp):
        self.image = image
        self.damage = damage
        self.mana_sp = mana_sp

Wearpon_info = {
    'bow': { 'image' : '', 'damage': 30, 'mana_sp': 5},
    'sword': {'image': '', 'damage': 40, 'mana_sp': 7}
}

player = []

def game():
    for v in player_info.values():
        p = Player(v['mana'], v['lives'], v['attack2'] )
        player.append(p)
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Player.attack1('hilichurl', 'bow', )
                    Vrazhina.attack1()
        Player.draw_pl(self='player')


        display.blit(bgfon, bgfon.get_rect())
        pg.display.update()
        clock.tick((FPS))

game()
pg.quit()

exit()
