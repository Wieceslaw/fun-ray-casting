from time import time
from numpy import array, float32
from time_test import time_test
import numpy as np
import numba as nb
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1- x2) ** 2 + (y1 - y2) ** 2)


def line(p1, p2):
    vec = p1 - p2
    if vec[0] == 0:
        vec[0] = 0.000001
    k = vec[1] / vec[0]
    b = p1[1] - p1[0] * k
    return k, b


def intersects(p0, p1, p2, ray_vec):
    x0, y0 = p0
    xr, yr = ray_vec
    k, b = line(p1, p2)
    temp = (yr - xr * k)
    if temp == 0: # parallel
        return
    t = (k * x0 + b - y0) / temp
    p3 = array((x0 + xr * t, y0 + yr * t))
    if t >= 0:
        length = distance(*p1, *p2)
        if distance(*p1, *p3) <= length and distance(*p2, *p3) <= length:
            return p3


def main():
    p1 = array((0, 3))
    p2 = array((3, 0))
    angle = 135
    ray = array((math.cos(math.pi * angle / 180), math.sin(math.pi * angle / 180)))
    print('ray', ray)
    p0 = array((0, 0))
    # print(numpy_distance(p1, p2))
    print(distance(2.33, 1.45, 7.43, 0.43))
    print(line(p1, p2))
    print('t:', intersects(p0, p1, p2, ray))


if __name__ == '__main__':
    main()