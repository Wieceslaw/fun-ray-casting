from pygame.draw import circle
from generate_random import *
from settings import *
from raycasting import *

lines = generate_random_lines(NLINES, SIZE)
points = generate_random_points(NPOINTS, SIZE) + lines_to_points(lines)
circles = generate_random_circles(NCIRCLES, RCIRCLE, SIZE)