import pygame

from settings3D import *
from objects import *
from functions import *

from app import App
from player import Player


class RayCast3DApp(App):
    def update(self):
        player.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        lines, circles
        pos = player.pos
        angle = player.angle
        collision_points = []
        if lines or circles:
            collision_points += raycast(pos, angle, FOV, NRAYS, lines, circles)
        for i, point in enumerate(collision_points):
            d = distance(pos, point) * math.cos((FOV / 2 - i * DANGLE) / 180 * math.pi)
            c = 1 / (1 + d * d * 0.00002)
            h = HEIGHT / d * COEFF
            color = tuple(array(WALLS_COLOR) * c)
            pygame.draw.rect(self.screen, color, (
                i * K,
                HALF_HEIGHT - h // 2,
                K,
                h 
            ))
        pygame.display.flip()


if __name__ == '__main__':
    app = RayCast3DApp(
        SIZE,
        FPS
    )
    player = Player(
        START_POS, 
        START_ANGLE, 
        MOVEMENT_SPEED, 
        ANGLE_SPEED,
        use_mouse=True
        )
    app.run()