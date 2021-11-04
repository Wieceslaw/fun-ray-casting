from numpy import array
from random import random


def generate_random_lines(n, size):
    return [(array((random() * size[0], random() * size[1])), array((random() * size[0], random() * size[1]))) for _ in range(n)]


def generate_random_points(n, size):
    return [array([random() * size[0], random() * size[1]]) for _ in range(n)]