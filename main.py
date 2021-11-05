import pygame
from numpy import array

from settings import *
from raycasting import *

from generate_random import generate_random_lines
from app import App


class RayCastApp(App):
    def update(self):
        keys()

    def draw(self):
        self.screen.fill(BG_COLOR)
        drawer(self.screen)
        pygame.display.flip()


def drawer(sc):
    pygame.draw.circle(sc, GREEN, cords, 12)
    # lines_in_fov = visible_lines(lines, cords, angle, FOV)
    # print(len(lines_in_fov), len(lines))
    for line in lines:
        pygame.draw.line(sc, GREEN, *line)
    # for line in lines_in_fov:
    #     pygame.draw.line(sc, RED, *line)
    # if len(lines_in_fov):
    #     collision_points = raycast(cords, angle, lines)
    # else:
    #     collision_points = []
    collision_points = raycast(cords, angle, lines)
    for collided, point in collision_points:
        if collided:
            pygame.draw.line(sc, RED, cords, point)
        else:
            pygame.draw.line(sc, BLUE, cords, point)


def keys():
    global cords, angle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cords[1] -= MOVEMENT_SPEED
    if keys[pygame.K_s]:
        cords[1] += MOVEMENT_SPEED
    if keys[pygame.K_a]:
        cords[0] -= MOVEMENT_SPEED
    if keys[pygame.K_d]:
        cords[0] += MOVEMENT_SPEED
    if keys[pygame.K_UP]:
        angle += ANGLE_SPEED
    if keys[pygame.K_DOWN]:
        angle -= ANGLE_SPEED


cords = array([400, 300])
lines = generate_random_lines(NLINES, SIZE)
angle = 0


if __name__ == '__main__':
    app = RayCastApp(
        SIZE,
        FPS
    )
    app.run()