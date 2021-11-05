from pygame.draw import circle
from generate_random import *
from settings import *

lines = generate_random_lines(NLINES, SIZE)
points = generate_random_points(NPOINTS, SIZE)
circles = generate_random_circles(NCIRCLES, RCIRCLE, SIZE)