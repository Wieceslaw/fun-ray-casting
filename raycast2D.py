import pygame

from settings import *
from objects import *
from functions import *

from app import App
from player import Player


class RayCastApp(App):
    def update(self):
        player.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        # drawing objects
        for line in lines:
            pygame.draw.line(self.screen, GREEN, *line)
        for point in points:
            pygame.draw.circle(self.screen, GREEN, point, RPOINT)
        for circle in circles:
            pygame.draw.circle(self.screen, GREEN, *circle)
        # drawing colliding lines
        collision_points = []
        pos = player.pos
        angle = player.angle
        if lines or circles:
            collision_points += raycast(pos, angle, FOV, NRAYS, lines, circles)
        for collided, point in collision_points:
            if collided:
                pygame.draw.line(self.screen, RED, pos, point)
            else:
                pygame.draw.line(self.screen, BLUE, pos, point)
        # drawing player
        pygame.draw.circle(self.screen, WHITE, pos, 12)
        pygame.display.flip()



if __name__ == '__main__':
    player = Player(START_POS, START_ANGLE, MOVEMENT_SPEED, ANGLE_SPEED)
    app = RayCastApp(
        SIZE,
        FPS
    )
    app.run()