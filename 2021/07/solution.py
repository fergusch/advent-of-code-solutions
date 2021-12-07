## advent of code 2021
## https://adventofcode.com/2021
## day 07

def parse_input(lines):
    return [int(x) for x in lines[0].strip().split(',')]

def part1(positions):
    min_cost = float('inf')
    for i in range(min(positions), max(positions)+1):
        fuel_cost = sum([abs(p-i) for p in positions])
        if fuel_cost < min_cost:
            min_cost = fuel_cost
    return min_cost

def part2(positions):
    min_cost = float('inf')
    for i in range(min(positions), max(positions)+1):
        fuel_cost = sum([int(abs(p-i)+(abs(p-i)*(abs(p-i)-1)/2)) for p in positions])
        if fuel_cost < min_cost:
            min_cost = fuel_cost
    return min_cost