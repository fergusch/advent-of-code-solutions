## advent of code 2021
## https://adventofcode.com/2021
## day 01
## ALT: using only list comprehensions

def parse_input(lines):
    return [int(x) for x in lines]

def part1(depths):
    return sum([depths[i] > depths[i-1] for i in range(1, len(depths))])

def part2(depths):
    return sum([sum(depths[i-2:i+1]) > sum(depths[i-3:i]) for i in range(3, len(depths))])