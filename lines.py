import pygame
from settings import *
from test import *
from numpy import array
from random import random

def generate_lines(n):
    return [(array((random() * SIZE[0], random() * SIZE[1])), array((random() * SIZE[0], random() * SIZE[1]))) for _ in range(n)]

cords = array([400, 300])
lines = generate_lines(100)


def drawer(sc):
    pygame.draw.circle(sc, GREEN, cords, 12)
    ray = array((math.cos(math.pi * angle / 180), math.sin(math.pi * angle / 180)))
    min_dist = 10000
    collieded = False
    for line in lines:
        pygame.draw.line(sc, GREEN, *line)
        t = intersects(cords, *line, ray)
        if t is not None:
            new_dist = distance(*cords, *t)
            if new_dist < min_dist:
                min_dist = new_dist
                point = t
            collieded = True
    if collieded:
        color = RED
    else:        
        point = cords + ray * 10000
        color = GREEN
    pygame.draw.line(sc, color, cords, point)


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