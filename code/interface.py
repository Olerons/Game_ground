import pygame
from settings import *


class Interface(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen

        self.footer = pygame.sprite.Sprite()
        self.img = pygame.Surface((WIDTH, HIGHT // 7)).fill((170, 170, 170))
        self.screen.blit(self.img)
        self.footer.rect = self.img.get_rect(buttomleft=(0, HIGHT))

        self.add(self.footer)

