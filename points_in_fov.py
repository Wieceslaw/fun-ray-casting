from numpy import array
from app import App
import pygame
from raycasting import *
from colors import *
from generate_random import *


class TestApp(App):
    def update(self):
        keys()
        updater()

    def draw(self):
        self.screen.fill(BLACK)
        drawer(self.screen)
        pygame.display.flip()


def drawer(screen):
    pygame.draw.circle(screen, GREEN, pos, 12)
    points_in_fov = visible_points(points, pos, angle, fov)
    left_edge = angle - fov // 2
    right_edge = angle + fov // 2
    pygame.draw.line(screen, GREEN, pos, pos + unit_vector(left_edge) * 1000)
    pygame.draw.line(screen, GREEN, pos, pos + unit_vector(right_edge) * 1000)
    for point in points:
        pygame.draw.circle(screen, BLUE, point, 5)
    for point in points_in_fov:
        pygame.draw.circle(screen, RED, point, 5)


def updater():
    pass


def keys():
    global pos, angle
    v = 1
    a_v = 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos[1] -= v
    if keys[pygame.K_s]:
        pos[1] += v
    if keys[pygame.K_a]:
        pos[0] -= v
    if keys[pygame.K_d]:
        pos[0] += v
    if keys[pygame.K_UP]:
        angle += a_v
    if keys[pygame.K_DOWN]:
        angle -= a_v


# settings
size = [400, 400]
pos = [200, 200]
angle = 0
fov = 120
points = generate_random_points(20, size)


if __name__ == '__main__':
    app = TestApp(
        size,
        60
    )
    app.run()