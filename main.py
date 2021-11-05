import pygame

from settings import *
from objects import *
from raycasting import *

from app import App


class RayCastApp(App):
    def update(self):
        keys()

    def draw(self):
        self.screen.fill(BG_COLOR)
        drawer(self.screen)
        pygame.display.flip()


def drawer(sc):
    for line in lines:
        pygame.draw.line(sc, GREEN, *line)
    for point in points:
        pygame.draw.circle(sc, GREEN, point, RPOINT)
    for circle in circles:
        pygame.draw.circle(sc, GREEN, *circle)
    # lines_in_fov = visible_lines(lines, pos, angle, FOV)
    # points_in_fov = visible_points(points, pos, angle, FOV)
    collision_points = []
    if lines or circles:
        collision_points += raycast(pos, angle, FOV, NRAYS, lines, circles)
    for collided, point in collision_points:
        if collided:
            pygame.draw.line(sc, RED, pos, point)
        else:
            pygame.draw.line(sc, BLUE, pos, point)
    pygame.draw.circle(sc, WHITE, pos, 12)


def keys():
    global pos, angle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos[1] -= MOVEMENT_SPEED
    if keys[pygame.K_s]:
        pos[1] += MOVEMENT_SPEED
    if keys[pygame.K_a]:
        pos[0] -= MOVEMENT_SPEED
    if keys[pygame.K_d]:
        pos[0] += MOVEMENT_SPEED
    if keys[pygame.K_UP]:
        angle += ANGLE_SPEED
    if keys[pygame.K_DOWN]:
        angle -= ANGLE_SPEED


if __name__ == '__main__':
    app = RayCastApp(
        SIZE,
        FPS
    )
    app.run()