import pygame
from settings import *

pygame.init()

def load_img(file, colorkey=None):
    img = pygame.image.load(file)
    if colorkey:
        img = img.convert()
        if colorkey == -1:
            colorkey = img.get_at((0, 0))
        img.set_colorkey(colorkey)
    else:
        img = img.convert_alpha()
    img = pygame.transform.scale(img, (TILESIZE, TILESIZE))
    return img


def import_brush(path, size):
    brush_list = []
    full_img = pygame.image.load(path)

    for y in range(0,full_img.get_size()[1], size[1]):
        for x in range(0,full_img.get_size()[0], size[0]):
            img = full_img.subsurface(pygame.Rect((x, y), size))
            brush_list.append(pygame.transform.scale(img, (TILESIZE, TILESIZE)))

    return brush_list