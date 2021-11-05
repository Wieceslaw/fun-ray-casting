import math
import pygame as pg
import numpy as np


class Player:
    def __init__(self, start_position: list or tuple, start_angle: int, movement_speed: int, angle_speed: int, use_mouse=False, rotational_control=False, strait_control=False):
        self.pos = np.array(start_position, dtype=float)
        self.angle = start_angle
        self.movement_speed = movement_speed
        self.angle_speed = angle_speed
        self.mouse_control = use_mouse
        self.rotational_control = rotational_control
        self.strait_control = strait_control
        self.movement_control = lambda x: None
        if self.mouse_control:
            pg.mouse.set_visible(False)
            pg.event.set_grab(True)
            self.movement_control = self.mouse_movement
        elif self.rotational_control:
            self.movement_control = self.rotational_movement
        elif self.strait_control:
            self.movement_control = self.strait_movement

    def update(self):
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_ESCAPE]:
            exit()
        self.movement_control(pressed_key)
    
    def mouse_movement(self, pressed_key):
        pg.mouse.set_pos(200, 200)
        self.angle += pg.mouse.get_rel()[0] / 10
        self.angle %= 360
        sin_a = math.sin(self.angle / 180 * math.pi)
        cos_a = math.cos(self.angle / 180 * math.pi)
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
    
    def rotational_movement(self, pressed_key):
        sin_a = math.sin(self.angle / 180 * math.pi)
        cos_a = math.cos(self.angle / 180 * math.pi)
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
            
    def strait_movement(self, pressed_key):
        if pressed_key[pg.K_LEFT]:
                self.angle -= self.angle_speed
        if pressed_key[pg.K_RIGHT]:
                self.angle += self.angle_speed
        if pressed_key[pg.K_w]:
            self.pos[1] -= self.movement_speed 
        if pressed_key[pg.K_s]:
            self.pos[1] += self.movement_speed
        if pressed_key[pg.K_a]:
            self.pos[0] -= self.movement_speed
        if pressed_key[pg.K_d]:
            self.pos[0] += self.movement_speed