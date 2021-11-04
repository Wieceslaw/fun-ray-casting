from numpy import array
from random import random
from settings import *


def generate_random_lines(n):
    return [(array((random() * SIZE[0], random() * SIZE[1])), array((random() * SIZE[0], random() * SIZE[1]))) for _ in range(n)]
