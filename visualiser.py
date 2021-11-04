import pygame
import math
from numpy import array, greater
from test import intersects

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60

angle = 0
cords = array([400, 300])
p1 = array([100, 200])
p2 = array([300, 400])


def draw():
    pygame.draw.circle(screen, GREEN, cords, 12)
    a = 1000
    ray = array((math.cos(math.pi * angle / 180), math.sin(math.pi * angle / 180)))
    if intersects(cords, p1, p2, ray):
        color = RED
    else:
        color = GREEN
    pygame.draw.line(screen, color, cords, cords + ray * a)
    pygame.draw.line(screen, GREEN, p1, p2)


def move():
    global cords, angle
    v = 1
    a_v = 0.5
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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(BLACK)
    move()
    draw()

    pygame.display.flip()
    clock.tick(FPS)