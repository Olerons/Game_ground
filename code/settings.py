WIDTH = 1530
HIGHT = 750

FPS = 60

TILESIZE = 64

TILES_COST = {
    'ground_water':5,
    'ground_ground':15,
    'build_wood':5,
    'build_house':25,
    'build_mill':50,
    'None':0
}

TILES_UP_INCOM = {
    'ground_water':0,
    'ground_ground':0,
    'build_wood':0,
    'build_house':5,
    'build_mill':10,
    'None':0
}

TILES_NEEDS = {
    'build_wood': {'ground_ground': 4},
    'build_house': {'ground_ground': 9},
    'build_mill': {'ground_ground' : 9}
}

TILES_PLACE = {
    'build_wood': 'ground_ground',
    'build_house': 'ground_ground',
    'build_mill': 'ground_ground'
}