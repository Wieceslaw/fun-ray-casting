import math
import pygame as pg
import numpy as np


class Player:
    def __init__(self, start_position: list or tuple, start_angle: int, movement_speed: int, angle_speed: int):
        self.pos = np.array(start_position, dtype=float)
        self.angle = start_angle
        self.movement_speed = movement_speed
        self.angle_speed = angle_speed

    def update(self):
        sin_a = math.sin(self.angle / 180 * math.pi)
        cos_a = math.cos(self.angle / 180 * math.pi)
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_LEFT]:
            self.angle -= self.angle_speed
        if pressed_key[pg.K_RIGHT]:
            self.angle += self.angle_speed
        if pressed_key[pg.K_w]:
            self.pos[0] += self.movement_speed * cos_a
            self.pos[1] += self.movement_speed * sin_a
        if pressed_key[pg.K_s]:
            self.pos[0] -= self.movement_speed * cos_a
            self.pos[1] -= self.movement_speed * sin_a
        if pressed_key[pg.K_a]:
            self.pos[0] += self.movement_speed * sin_a
            self.pos[1] -= self.movement_speed * cos_a
        if pressed_key[pg.K_d]:
            self.pos[0] -= self.movement_speed * sin_a
            self.pos[1] += self.movement_speed * cos_a