## advent of code 2021
## https://adventofcode.com/2021
## day 11

import numpy as np

def parse_input(lines):
    return np.array([[int(x) for x in line] for line in lines])

def get_neighbors(y, x, data):
    neighbors = []
    for dy, dx in [(y, x) for y in range(-1, 2) for x in range(-1, 2)]:
        if (dy, dx) == (0, 0): 
            continue
        if y+dy >= 0 and y+dy < len(data) and x+dx >= 0 and x+dx < len(data[0]):
            neighbors.append((y+dy, x+dx))
    return neighbors

def part1(data):
    octopi = data.copy()
    flashes = 0
    for n in range(100):
        for y, row in enumerate(octopi):
            for x, col in enumerate(row):
                octopi[y][x] += 1
        while np.any(octopi > 9):
            for y, row in enumerate(octopi):
                for x, col in enumerate(row):
                    if octopi[y][x] > 9:
                        octopi[y][x] = 0
                        flashes += 1
                        for ny, nx in get_neighbors(y, x, octopi):
                            if octopi[ny][nx] > 0:
                                octopi[ny][nx] += 1
    return flashes

def part2(data):
    octopi = data.copy()
    n = 0
    while not np.all(octopi == 0):
        for y, row in enumerate(octopi):
            for x, col in enumerate(row):
                octopi[y][x] += 1
        while np.any(octopi > 9):
            for y, row in enumerate(octopi):
                for x, col in enumerate(row):
                    if octopi[y][x] > 9:
                        octopi[y][x] = 0
                        for ny, nx in get_neighbors(y, x, octopi):
                            if octopi[ny][nx] > 0:
                                octopi[ny][nx] += 1
        n += 1
    return n