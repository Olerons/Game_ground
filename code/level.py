import pygame
from settings import *
from tile import Tile
from debug import debug
from helper_def import import_brush
from interface import Interface


class Level:
    def __init__(self, interface):
        self.screen = pygame.display.get_surface()

        self.brush = import_brush('../data/img/basictiles2.png', (16, 16))

        self.bg_sprites = pygame.sprite.Group()
        self.ground_sprites = Ground_group()
        self.build_sprites = Build_group()
        self.cursor_sprites = Cursor_group(self.bg_sprites)
        self.object_sprites = pygame.sprite.Group()
        self.interface = interface

        self.create_map()

    def create_map(self):
        for row in range(100):
            for col in range(100):
                x = TILESIZE * col
                y = TILESIZE * row
                Tile((x, y), [self.bg_sprites], type='bg')

    def draw(self, mouse_pos):
        self.bg_sprites.draw(self.screen)
        self.ground_sprites.draw(self.screen)
        self.build_sprites.draw(self.screen)
        self.cursor_sprites.draw(mouse_pos)
        self.interface.draw(self.screen)

    def click(self, mouse):
        key = False
        interface_type = self.interface.get_type()
        for ground_sp in self.ground_sprites:
            if ground_sp.rect.collidepoint(mouse) and interface_type:
                self.build_sprites.update(ground_sp, interface_type)
                key = True
        if not key:
            if mouse[1] < HIGHT - HIGHT // 5:
                for sprite in self.bg_sprites:
                    if sprite.rect.collidepoint(mouse) and interface_type:
                        self.ground_sprites.update(sprite, interface_type)


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
                img.set_alpha(100)
                self.screen.blit(img, sprite.rect)


class Ground_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.ground_types = ['ground_water', 'ground_ground']
        self.screen = pygame.display.get_surface()

    def update(self, sprite, type_tile):
        if type_tile not in self.ground_types:
            return
        x, y = sprite.rect.left, sprite.rect.top
        flag = True
        for g_sprite in self.sprites():
            if g_sprite.rect.collidepoint((x+1,y+1)):
                if g_sprite.type != type_tile:
                    g_sprite.kill()
                    Tile((x, y), [self], type=type_tile)
                flag = False
        if flag:
            Tile((x, y), [self], type=type_tile)


class Build_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.build_types = ['build_wood', 'build_house', 'build_mill']

    def update(self, sprite, type_tile):
        if type_tile not in self.build_types:
            return
        x, y = sprite.rect.left, sprite.rect.top




        flag = True
        for g_sprite in self.sprites():
            if g_sprite.rect.collidepoint((x + 1, y + 1)):
                if g_sprite.type != type_tile:
                    g_sprite.kill()
                    Tile((x, y), [self], type=type_tile)
                flag = False
        if flag:
            Tile((x, y), [self], type=type_tile)
