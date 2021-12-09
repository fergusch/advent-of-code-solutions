## advent of code 2021
## https://adventofcode.com/2021
## day 09

import numpy as np
from functools import reduce

def parse_input(lines):
    return np.array([[int(x) for x in list(line)] for line in lines])

def get_neighbors(arr, y, x):
    neighbors = []
    if x > 0:
        neighbors.append((y, x-1))
    if x < len(arr[0])-1:
        neighbors.append((y, x+1))
    if y > 0:
        neighbors.append((y-1, x))
    if y < len(arr)-1:
        neighbors.append((y+1, x))
    return neighbors

def part1(hmap):
    risk = 0
    for y, row in enumerate(hmap):
        for x, col in enumerate(row):
            if np.all(hmap[y][x] < [hmap[ny][nx] for ny, nx in get_neighbors(hmap, y, x)]):
                risk += 1 + hmap[y][x]
    return risk

def part2(hmap):

    def bfs(y, x):
        if hmap[y][x] == 9: return [(y, x)]
        q, visited = [(y,x)], [(y,x)]
        while q:
            y, x = q.pop()
            for ny, nx in get_neighbors(hmap, y, x):
                if hmap[ny][nx] < 9 and (ny, nx) not in visited:
                    visited.append((ny, nx))
                    q.insert(0, (ny, nx))
        return visited
    
    searched_from = []
    basin_sizes = []
    for y, row in enumerate(hmap):
        for x, col in enumerate(row):
            if (y, x) not in searched_from:
                basin = bfs(y, x)
                searched_from += basin
                basin_sizes.append(len(basin))

    top_three = sorted(basin_sizes, reverse=True)[:3]
    return reduce(lambda x, y: x * y, top_three)