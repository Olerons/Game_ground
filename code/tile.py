import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type=None):
        super().__init__(groups)
        if type == 'bg':
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            #pygame.draw.rect(self.image, pg.Color("Green"), (x, y, width, height), width=border_width)
            self.image.fill((100, 100, 100))
            self.image.fill((200,200,200), (1,1,TILESIZE-2,TILESIZE-2))

        self.rect = self.image.get_rect(topleft=pos)
