## advent of code 2021
## https://adventofcode.com/2021
## day 01

def parse_input(lines):
    return [int(x) for x in lines]

def part1(depths):
    count = 0
    for i, depth in enumerate(depths):
        if i == 0: continue
        if depths[i] > depths[i-1]:
            count += 1
    return count

def part2(depths):
    count = 0
    prev_window = float('inf')
    for i, depth in enumerate(depths):
        if i < 2: continue
        window = sum(depths[i-2:i+1])
        if window > prev_window:
            count += 1
        prev_window = window
    return count