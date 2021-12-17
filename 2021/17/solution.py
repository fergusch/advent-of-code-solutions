## advent of code 2021
## https://adventofcode.com/2021
## day 17

import re

def parse_input(lines):
    return [(int(a), int(b)) for a, b in re.findall('(?:x|y)=(-?\d+)\.\.(-?\d+)', lines[0])]

def simulate(dx, dy, x_range, y_range):
    x, y = 0, 0
    max_y = float('-inf')
    while True:
        x += dx
        y += dy
        if y > max_y:
            max_y = y
        dx -= (1 if dx>0 else -1 if dx<0 else 0)
        dy -= 1
        if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
            # in target range
            return max_y
        elif x > x_range[1] or y < y_range[0]:
            # missed
            return None

def part1(data):
    # don't worry, I hate this too
    # but it does work
    max_y = float('-inf')
    for dx in range(100):
        for dy in range(100):
            result = simulate(dx, dy, data[0], data[1])
            if result is not None and result > max_y:
                max_y = result
    return max_y

def part2(data):
    prev_total = float('-inf')
    for n in range(0, 1000, 200):
        total = 0
        for dx in range(n):
            for dy in range(-n, n):
                result = simulate(dx, dy, data[0], data[1])
                if result is not None:
                    total += 1
        # once the total stops increasing,
        # no need to continue simulating
        if total > prev_total:
            prev_total = total
        elif total == prev_total:
            return total
