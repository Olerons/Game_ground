import pygame.sprite

#WIDTH = 1530
#HIGHT = 750
pygame.display.set_mode((1530,750), flags=pygame.FULLSCREEN)
WIDTH, HIGHT = pygame.display.get_window_size()

ALL_SPRITES = pygame.sprite.Group()

FPS = 60

TILESIZE = 64

TILES_COST = {
    'ground_water':5,
    'ground_ground':15,
    'build_wood':5,
    'build_house':25,
    'build_mill':70,
    'None':0
}

TILES_UP_INCOM = {
    'ground_water':(0,0),
    'ground_ground':(0,0),
    'build_wood':(1,0),
    'build_house':(3,5),
    'build_mill':(7,0),
    'None':(0,0)
}

TILES_NEEDS = {
    'build_wood': {'ground_ground': 4},
    'build_house': {'ground_ground': 4, 'ground_water': 2},
    'build_mill': {'ground_ground' : 9, 'build_wood':3}
}

TILES_PLACE = {
    'build_wood': 'ground_ground',
    'build_house': 'ground_ground',
    'build_mill': 'ground_ground'
}