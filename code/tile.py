import pygame
from settings import *
from helper_def import import_brush
from random import choice


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type='', image=pygame.surface.Surface((TILESIZE,TILESIZE)), animated=False):
        super().__init__(groups)
        self.type = type
        self.image = image
        self.income_plus = 0
        self.place = ''
        self.needs = {}
        self.animated = animated

        if type == 'bg':
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            #pygame.draw.rect(self.image, pg.Color("Green"), (x, y, width, height), width=border_width)
            self.image.fill((100, 100, 100))
            self.image.fill((200,200,200), (1,1,TILESIZE-2,TILESIZE-2))

        elif type == 'ground_water':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[choice([171, 172])] # water
            self.animated_list = [self.brush[choice([171, 172])], self.brush[choice([171, 172])], self.brush[choice([171, 172])], self.brush[choice([171, 172])]]
            self.animated_tick = 70
            self.animated_index = 0
            self.animated = True

        elif type == 'ground_ground':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[choice([45, 46])] # ground

        elif type == 'build_wood':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[91]
            self.place = 'ground_ground'
            self.needs = {'ground_ground': 4}

        elif type == 'build_house':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[19]
            self.income_plus = 5
            self.place = 'ground_ground'
            self.needs = {'ground_ground': 9}

        elif type == 'build_mill':
            self.brush = import_brush('../data/img/basictiles2.png', (16, 16))
            self.image = self.brush[100]
            self.income_plus = 5
            self.place = 'ground_ground'
            self.needs = {'ground_ground': 9}

        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        if self.animated:
            if self.animated_tick <= 0:
                self.animated_index = (self.animated_index + 1) % len(self.animated_list)
                self.image = self.animated_list[self.animated_index]
                self.animated_tick = 70
            self.animated_tick -= 1