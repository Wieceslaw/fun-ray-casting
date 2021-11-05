from colors import *

# app config
FPS = 60
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
BG_COLOR = BLACK

# consts
INFINITY = 10e10

# player config
START_POS = (0, 0)
START_ANGLE = 0
ANGLE_SPEED = 1
MOVEMENT_SPEED = 2

# object settings
NLINES = 10
NPOINTS = 0
NCIRCLES = 5
RPOINT = 3
RCIRCLE = 50

# other
MAX_LENGTH = (SIZE[0] ** 2 + SIZE[1] ** 2) ** 0.5
FOV = 60
NRAYS = 120
DANGLE = FOV / NRAYS