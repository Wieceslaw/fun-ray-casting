from colors import *
from numpy import array

# app config
FPS = 60
SIZE = (800, 600)
BG_COLOR = BLACK

# consts
INFINITY = 10e10

# object settings
NLINES = 10
NPOINTS = 0
NCIRCLES = 5
RPOINT = 3
RCIRCLE = 50

MAX_LENGTH = (SIZE[0] ** 2 + SIZE[1] ** 2) ** 0.5
ANGLE_SPEED = 1
MOVEMENT_SPEED = 2
FOV = 120
NRAYS = 120

DANGLE = FOV / NRAYS

pos = array([400, 300])
angle = 0