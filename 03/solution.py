## advent of code 2020
## https://adventofcode.com/2020
## day 3

with open('input.txt', 'r') as f:
    map = [list(x.strip()) for x in f.readlines()]

# part one ------------------------------------------------

x, y = (0, 0)
trees = 0

while y < len(map):
    if map[y][x] == '#':
        trees += 1
    if x+3 >= len(map[0]):
        x = 3 - (len(map[0]) - x)
    else:
        x += 3
    y += 1

print(trees)

# part two ------------------------------------------------

from operator import mul
from functools import reduce

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []

for slope in slopes:

    x, y = (0, 0)
    trees = 0

    while y < len(map):
        if map[y][x] == '#':
            trees += 1
        if x+slope[0] >= len(map[0]):
            x = slope[0] - (len(map[0]) - x)
        else:
            x += slope[0]
        y += slope[1]

    results.append(trees)

print(reduce(mul, results, 1))