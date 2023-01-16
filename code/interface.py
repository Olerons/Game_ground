import pygame
from settings import *
from helper_def import import_brush


class Interface(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.add(Footer())

        self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
        self.btn_water = self.brush[171] # water
        self.add(Button((15,HIGHT-15),(100, 100),'test', self.btn_water))

        self.btn_ground = self.brush[45]  # ground
        self.add(Button((130, HIGHT - 15), (100, 100), 'test', self.btn_ground))

    def active(self):
        pass


class Footer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH, HIGHT//6))
        self.image.fill((150,50,15))
        self.rect = self.image.get_rect(bottomleft=(0,HIGHT))


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
