import math
from numba.np.ufunc import parallel
from numpy import array
import numba as nb
import numpy as np

from settings import *
from generate_random_lines import generate_random_lines


@nb.njit(fastmath=True)
def distance(p1, p2):
    return np.sqrt((p1[0]- p2[0]) ** 2 + (p1[1]- p2[1]) ** 2)


@nb.njit(parallel=True)
def line(p1, p2):
    vec = p1 - p2
    if vec[0] == 0:
        vec[0] = 10e-10
    k = vec[1] / vec[0]
    b = p1[1] - p1[0] * k
    return k, b


@nb.njit
def intersection(p0, p1, p2, ray_vec):
    x0, y0 = p0
    xr, yr = ray_vec
    k, b = line(p1, p2)
    temp = (yr - xr * k)
    if temp == 0:
        return
    t = (k * x0 + b - y0) / temp
    p3 = array((x0 + xr * t, y0 + yr * t))
    if t >= 0:
        length = distance(p1, p2)
        if distance(p1, p3) <= length and distance(p2, p3) <= length:
            return p3


def right_or_left(p0, p1, vec0):
    vec1 = p1 - p0
    return 1 if np.cross(vec0, vec1) >= 0 else -1


@nb.njit(fastmath=True)
def unit_vector(angle):
    return array([math.cos(angle / 180 * math.pi), math.sin(angle / 180 * math.pi)])


def visible_lines(lines, pos, angles):
    _lines = []
    vec0 = unit_vector(angles[0])
    vec1 = unit_vector(angles[1])
    for line in lines:
        if (right_or_left(pos, line[0], vec0) >= 0 \
        and right_or_left(pos, line[0], vec1) < 0) \
       or (right_or_left(pos, line[1], vec0) >= 0 \
        and right_or_left(pos, line[1], vec1)) < 0:
            _lines.append(line)
    return _lines


@nb.njit
def raycast(ray_point: array, angle: int, lines: list):
    points = []
    for ang in range(angle - FOV // 2, angle + FOV // 2, FOV // NRAYS):
        vec = unit_vector(ang)
        min_dist = INFINITY
        nearest_point = vec * MAX_LENGTH + ray_point
        collided = False
        for line in lines:
            point = intersection(ray_point, *line, vec)
            if point is not None:
                collided = True
                new_dist = distance(ray_point, point)
                if new_dist < min_dist:
                    min_dist = new_dist
                    nearest_point = point
        points.append((collided, nearest_point))
    return points


def main():
    lines = [((0,1), (0,2)), ((0,3), (0,4))]

    # visible_lines(lines, 1, 1)
    p0 = array([1, 0])
    pos = array([0, 0])
    vec = array([1, 1])
    # print(right_or_left(pos, p0, vec))
    angle = 90
    print(visible_lines(lines, pos, (angle - NRAYS // 2, angle + NRAYS // 2)))

if __name__ == '__main__':
    main()