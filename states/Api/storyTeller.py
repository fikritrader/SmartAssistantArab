import random

def random_line(fname):
    lines = open(fname).read().split("$$")
    return random.choice(lines)

