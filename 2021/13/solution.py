## advent of code 2021
## https://adventofcode.com/2021
## day 13

import numpy as np
import re

def parse_input(lines):
    coords = [[int(x) for x in re.findall('(\d+)', line)] for line in lines
              if not line.startswith('fold')]
    max_x, max_y = list(map(max, zip(*coords)))
    paper = np.full((max_x+1, max_y+1), False, dtype=bool)
    for y, x in coords:
        paper[y][x] = True
    folds = [(f[0], int(f[1])) for line in lines for f in re.findall('(y|x)=(\d+)', line)]
    return np.transpose(paper), folds

def fold_along_y(paper, y):
    m = paper.copy()
    flipped = np.flip(m[y+1:], axis=0)
    # pad folded part if lengths don't match
    if flipped.shape[0] != m[:y].shape[0]:
        flipped = np.pad(flipped, ((1,0), (0,0)))
    return np.add(m[:y], flipped)

def part1(paper, folds):
    m = paper.copy()
    f = folds.copy()[:1]
    for axis, val in f:
        if axis == 'y':
            m = fold_along_y(m, val)
        elif axis == 'x':
            m = np.transpose(fold_along_y(np.transpose(m), val))
    return np.sum(m)

def part2(paper, folds):
    m = paper.copy()
    f = folds.copy()
    for axis, val in f:
        if axis == 'y':
            m = fold_along_y(m, val)
        elif axis == 'x':
            m = np.transpose(fold_along_y(np.transpose(m), val))
    print(np.array2string(np.array(m, dtype=int)).replace('1\n ', '1').replace('0', ' ').replace('1', '#'))
    return 'ZUJUAFHP'