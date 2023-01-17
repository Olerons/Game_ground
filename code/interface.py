import pygame
from settings import *
from helper_def import import_brush, load_img


class Interface(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.footer = Footer()
        self.add(Footer())

        self.brush = import_brush('../data/img/basictiles2.png', (16, 16))

        self.btn_water = Button((15,HIGHT-15),(100, 100),'ground_water', self.brush[171]) # water
        self.add(self.btn_water)

        self.btn_ground = Button((130, HIGHT - 15), (100, 100), 'ground_ground', self.brush[45])  # ground
        self.add(self.btn_ground)

    def active(self):
        pass


class Footer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_img('../data/img/footer.png', tile=False)
        self.image = pygame.transform.scale(self.image, (WIDTH // 2, HIGHT // 5))
        self.rect = self.image.get_rect(midbottom=(WIDTH//2,HIGHT))


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, action, img=None):
        super().__init__()
        if img:
            self.image = pygame.Surface(size)
            self.image.fill((20,20,20))
            self.image.blit(pygame.transform.scale(img, (size[0]-4,size[1]-4)), (2,2))
        else:
            self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(bottomleft=pos)

        self.status = False
        self.action = action
