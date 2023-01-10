import pygame
from settings import *
from tile import Tile
from debug import debug
from helper_def import import_brush


class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.brush = import_brush('../data/img/basictiles2.png', (16, 16))

        self.bg_sprites = pygame.sprite.Group()
        self.ground_sprites = Ground_group(self.bg_sprites)
        self.build_sprites = pygame.sprite.Group()
        self.cursor_sprites = Cursor_group(self.bg_sprites)
        self.object_sprites = pygame.sprite.Group()
        self.interface_sprite = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row in range(100):
            for col in range(100):
                x = TILESIZE * col
                y = TILESIZE * row
                Tile((x, y), [self.bg_sprites], type='bg')

    def draw(self, mouse_pos):
        self.ground_sprites.update(mouse_pos)

        self.bg_sprites.draw(self.screen)
        self.cursor_sprites.draw(mouse_pos)
        self.ground_sprites.draw(self.screen)


class Cursor_group(pygame.sprite.Group):
    def __init__(self, bg_group):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.bg_sprites = bg_group

    def draw(self, mouse_pos):
        debug(mouse_pos)
        for sprite in self.bg_sprites:
            if sprite.rect.collidepoint(mouse_pos):
                img = pygame.Surface((TILESIZE, TILESIZE))
                img.fill('green')
                self.screen.blit(img, sprite.rect)


class Ground_group(pygame.sprite.Group):
    def __init__(self, bg_group):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.bg_sprites = bg_group

    def update(self, mouse_pos):
        self.mouse_key = pygame.mouse.get_pressed()
        if self.mouse_key[0]:
            for sprite in self.bg_sprites:
                if sprite.rect.collidepoint(mouse_pos):
                    Tile((sprite.rect.x, sprite.rect.y), [self], type='ground_w')