import pygame
from numpy import array

from settings import *
from raycasting import *
from generate_random_lines import generate_random_lines

cords = array([400, 300])
lines = generate_random_lines(NLINES)

def drawer(sc):
    pygame.draw.circle(sc, GREEN, cords, 12)
    for line in lines:
        pygame.draw.line(sc, GREEN, *line)
    collision_points = raycast(cords, angle, lines)
    for collided, point in collision_points:
        if collided:
            pygame.draw.line(sc, RED, cords, point)
        else:
            pygame.draw.line(sc, BLUE, cords, point)


angle = 0
def keys():
    global cords, angle
    v = MOVEMENT_SPEED
    a_v = ANGLE_SPEED
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cords[1] -= v
    if keys[pygame.K_s]:
        cords[1] += v
    if keys[pygame.K_a]:
        cords[0] -= v
    if keys[pygame.K_d]:
        cords[0] += v
    if keys[pygame.K_UP]:
        angle += a_v
    if keys[pygame.K_DOWN]:
        angle -= a_v