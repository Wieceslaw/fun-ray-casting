import pygame
from numpy import array

from settings import *
from raycasting import *
from generate_random import generate_random_lines

cords = array([400, 300])
lines = generate_random_lines(NLINES, SIZE)
angle = 0


def drawer(sc):
    pygame.draw.circle(sc, GREEN, cords, 12)
    lines_in_fov = visible_lines(lines, cords, angle, FOV)
    print(len(lines_in_fov), len(lines))
    for line in lines_in_fov:
        pygame.draw.line(sc, GREEN, *line)
    if len(lines_in_fov):
        collision_points = raycast(cords, angle, lines_in_fov)
    else:
        collision_points = []
    for collided, point in collision_points:
        if collided:
            pygame.draw.line(sc, RED, cords, point)
        else:
            pygame.draw.line(sc, BLUE, cords, point)


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