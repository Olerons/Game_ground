import pygame
from settings import *
from helper_def import import_brush
from random import choice


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type='', image=pygame.surface.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.type = type
        self.image = image
        if type == 'bg':
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            #pygame.draw.rect(self.image, pg.Color("Green"), (x, y, width, height), width=border_width)
            self.image.fill((100, 100, 100))
            self.image.fill((200,200,200), (1,1,TILESIZE-2,TILESIZE-2))

        elif type == 'ground_water':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[choice([171, 172])] # water

        elif type == 'ground_ground':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[45] # water

        elif type == 'build_wood':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[173]

        self.rect = self.image.get_rect(topleft=pos)

