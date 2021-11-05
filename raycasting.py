import math
import numpy as np
import numba as nb
from numpy import array

from settings import *


@nb.njit(fastmath=True)
def distance(p1, p2):
    return np.sqrt((p1[0]- p2[0]) ** 2 + (p1[1]- p2[1]) ** 2)


def right_or_left(p0, p1, vec0):
    vec1 = p1 - p0
    return 1 if np.cross(vec0, vec1) >= 0 else -1


@nb.njit(fastmath=True)
def unit_vector(angle):
    return array([math.cos(angle / 180 * math.pi), math.sin(angle / 180 * math.pi)])


def visible_lines(lines, pos, angle, fov):
    _lines = []
    vec0 = unit_vector(angle + 90)
    # vec1 = unit_vector(angle - fov / 2)
    # vec2 = unit_vector(angle + fov / 2)
    for line in lines:
        # # point 1 lies in fov
        # cond1 = (right_or_left(pos, line[0], vec1) >= 0) and (right_or_left(pos, line[0], vec2) < 0)
        # # point 2 lies in fov
        # cond2 = (right_or_left(pos, line[1], vec1) >= 0) and (right_or_left(pos, line[1], vec2) < 0)
        
        # one point lies in fov = 180
        cond3 = (right_or_left(pos, line[0], vec0) < 0) or \
                (right_or_left(pos, line[1], vec0) < 0)
    
        if cond3:
            _lines.append(line)
    return _lines


def visible_points(points, pos, angle, fov):
    result = []
    vec0 = unit_vector(angle - fov / 2)
    vec1 = unit_vector(angle + fov / 2)
    for point in points:
        if right_or_left(pos, point, vec0) > 0 \
        and right_or_left(pos, point, vec1) < 0:
            result.append(point)
    return result


def rotate_vector(vec):
    return array([vec[1], -vec[0]])


@nb.njit
def line_raycast(ray_point: array, angle: int, lines: list):
    points = []
    ang = angle - FOV // 2
    for _ in range(NRAYS):
        ang += DANGLE
        vec = unit_vector(ang)
        min_dist = INFINITY
        nearest_point = vec * MAX_LENGTH + ray_point
        collided = False
        for line in lines:
            point = line_intersection(ray_point, vec, line)
            if point is not None:
                collided = True
                new_dist = distance(ray_point, point)
                if new_dist < min_dist:
                    min_dist = new_dist
                    nearest_point = point
        points.append((collided, nearest_point))
    return points


@nb.njit
def line_intersection(p0, ray, line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    x3, y3 = p0
    x4, y4 = p0 + ray
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    if t > 1 or t < 0:
        return
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    if u < 0:
        return
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)
    return array([x, y])


def lines_to_points(lines):
    points = []
    for line in lines:
        for point in line:
            points.append(point)
    return points


def prove_circle_intersection(pos, ray, circle):
    p0, r = circle
    vec0 = p0 - pos
    vec1 = (np.dot(vec0, ray) / np.dot(ray, ray)) * ray
    p1 = pos + vec1
    if distance(p0, p1) <= r:
        return True


def circle_intersection(pos: array, ray: array, circle: int) -> array:
    p0, r = circle
    x0, y0 = pos
    x1, y1 = pos + ray
    h, k = p0
    a = (x1 - x0) ** 2 + (y1 - y0) ** 2
    if a == 0:
        return
    b = 2 * (x1 - x0) * (x0 - h) + 2 * (y1 - y0) * (y0 - k)
    c = (x0 - h) ** 2 + (y0 - k) ** 2 - r ** 2
    if b ** 2 - 4 * a * c < 0:
        return
    t1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a) 
    x = x0 + t1 * (x1 - x0)
    y = y0 + t1 * (y1 - y0)
    if t1 > 0:
        return array([x, y])


def circle_raycast(pos: array, angle: int, circles: list):
    points = []
    ang = angle - FOV // 2
    for _ in range(NRAYS):
        ang += DANGLE
        ray = unit_vector(ang)
        min_dist = INFINITY
        nearest_point = ray * 1000 + pos
        collided = False
        for circle in circles:
            point = circle_intersection(pos, ray, circle)
            if point is not None:
                collided = True
                new_dist = distance(pos, point)
                if new_dist < min_dist:
                    min_dist = new_dist
                    nearest_point = point
        points.append((collided, nearest_point))
    return points


def raycast(pos, angle, fov, nrays, lines=[], circles=[]):
    points = []
    dangle = fov / nrays
    ang = angle - fov // 2
    for _ in range(nrays):
        ang += dangle
        ray = unit_vector(ang)
        min_dist = INFINITY
        nearest_point = ray * 1000 + pos
        collided = False
        for circle in circles:
            point = circle_intersection(pos, ray, circle)
            if point is not None:
                collided = True
                new_dist = distance(pos, point)
                if new_dist < min_dist:
                    min_dist = new_dist
                    nearest_point = point
        for line in lines:
            point = line_intersection(pos, ray, line)
            if point is not None:
                collided = True
                new_dist = distance(pos, point)
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