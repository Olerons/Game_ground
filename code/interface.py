import pygame
from settings import *
from helper_def import import_brush, load_img


class Interface(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.vector = 0

        self.footer = Footer()
        self.add(Footer())

        self.brush = import_brush('../data/img/basictiles2.png', (16, 16))

        btn_water = Button((self.footer.rect.centerx + 50, self.footer.rect.centery),(75, 75),'ground_water', self.brush[171]) # water
        self.add(btn_water)

        btn_ground = Button((self.footer.rect.centerx - 50, self.footer.rect.centery), (75, 75), 'ground_ground', self.brush[45])  # ground
        self.add(btn_ground)

        self.btn_list = [btn_water, btn_ground]

        self.coin = Coin((WIDTH, 0), (60,60))
        self.add(self.coin)

        btn_direction_up = Button_direction((self.footer.rect.right+30, self.footer.rect.centery-30), (50, 50), 'btn_up', load_img('../data/img/up_btn.png', tile=False))
        btn_direction_down = Button_direction((self.footer.rect.right+30, self.footer.rect.centery+30), (50, 50), 'btn_down', load_img('../data/img/down_btn.png', tile=False))
        self.add(btn_direction_up)
        self.add(btn_direction_down)
        self.btn_direction = [btn_direction_up, btn_direction_down]

    def get_type(self):
        for btn in self.btn_list:
            if btn.status:
                return btn.type

    def click(self, mouse):
        if self.footer.rect.collidepoint(mouse):
            for btn in self.btn_list:
                if btn.rect.collidepoint(mouse):
                    btn.status = True
                else:
                    btn.status = False
        elif self.btn_direction[0].rect.collidepoint(mouse):
            self.btn_list = self.swap_btn(-1)
        elif self.btn_direction[1].rect.collidepoint(mouse):
            self.btn_list = self.swap_btn(1)

    def swap_btn(self, vector):
        for btn in self.btn_list:
            btn.kill()
        if vector == -1:
            btn_water = Button((self.footer.rect.centerx + 50, self.footer.rect.centery), (75, 75), 'ground_water', self.brush[171])  # water
            self.add(btn_water)

            btn_ground = Button((self.footer.rect.centerx - 50, self.footer.rect.centery), (75, 75), 'ground_ground', self.brush[45])  # ground
            self.add(btn_ground)
            return [btn_water, btn_ground]

        if vector == 1:
            btn_wood = Button((self.footer.rect.centerx + 50, self.footer.rect.centery), (75, 75), 'build_wood', self.brush[173])  # wood
            self.add(btn_wood)
            return [btn_wood]


class Footer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_img('../data/img/footer.png', tile=False)
        self.image = pygame.transform.scale(self.image, (WIDTH // 2, HIGHT // 5))
        self.rect = self.image.get_rect(midbottom=(WIDTH//2,HIGHT))


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, type='', img=None):
        super().__init__()
        self.size = size
        self.img = img
        if img:
            self.image = pygame.Surface(size)
            self.image.fill((20,20,20))
            self.image.blit(pygame.transform.scale(img, (size[0]-4,size[1]-4)), (2,2))
        else:
            self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(center=pos)

        self.status = False
        self.type = type

    def update(self):
        if self.status:
            self.image = pygame.Surface(self.size)
            self.image.fill((20, 20, 20))
            self.image.blit(pygame.transform.scale(self.img, (self.size[0] - 8, self.size[1] - 8)), (4, 4))
        else:
            self.image = pygame.Surface(self.size)
            self.image.fill((20, 20, 20))
            self.image.blit(pygame.transform.scale(self.img, (self.size[0] - 2, self.size[1] - 2)), (1, 1))

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.pos = pos
        self.size = size
        self.coin = 10
        self.incom = 200
        self.incom_tick = 200

        self.font = pygame.font.Font('../data/PressStart2P.ttf', 25)
        self.image = pygame.Surface((self.size[0]*2, self.size[1]), pygame.SRCALPHA)

        self.img = load_img('../data/img/moneta.png', tile=False)
        self.img = pygame.transform.scale(self.img, self.size)
        self.image.blit(self.img, (size[0],0))

        coin_txt = self.font.render(str(self.coin), True, (180, 0, 0))
        coin_rect = coin_txt.get_rect(midleft=(0, size[1]//2))
        self.image.blit(coin_txt, coin_rect)

        self.rect = self.image.get_rect(topright=pos)

    def update(self):
        if self.incom_tick <= 0:
            self.coin += 1

            coin_txt = self.font.render(str(self.coin), True, (180, 0, 0))
            coin_rect = coin_txt.get_rect(midleft=(0, self.size[1] // 2))

            empty = pygame.Color(0, 0, 0, 0)
            self.image.fill(empty, (0,0,self.size[0], self.size[1]))
            self.image.blit(coin_txt, coin_rect)

            self.incom_tick = self.incom
        else:
            self.incom_tick -= 1


class Button_direction(pygame.sprite.Sprite):
    def __init__(self, pos, size, type, img):
        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(img, size)

        self.rect = self.image.get_rect(center=pos)

        self.status = False
        self.type = type

