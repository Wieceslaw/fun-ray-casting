from settings import *
from numpy import array
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1- x2) ** 2 + (y1 - y2) ** 2)


def line(p1, p2):
    vec = p1 - p2
    if vec[0] == 0:
        vec[0] = 10e-10
    k = vec[1] / vec[0]
    b = p1[1] - p1[0] * k
    return k, b


def intersection(p0, p1, p2, ray_vec):
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


def raycast(ray_point, angle, lines):
    points = []
    for ang in range(angle - NRAYS // 2, angle + NRAYS // 2):
        ray = array((math.cos(math.pi * ang / 180), math.sin(math.pi * ang / 180)))
        min_dist = INFINITY
        nearest_point = ray * MAX_LENGTH + ray_point
        collided = False
        for line in lines:
            point = intersection(ray_point, *line, ray)
            if point is not None:
                collided = True
                new_dist = distance(*ray_point, *point)
                if new_dist < min_dist:
                    min_dist = new_dist
                    nearest_point = point
        points.append((collided, nearest_point))
    return points


def main():
    cords = array([0, 0])
    angle = 0
    lines = generate_lines(10)
    lines = [(array([-2, 2]), array([2, 2]))]
    sp = raycast(cords, angle, lines)
    print(sp)


if __name__ == '__main__':
    main()