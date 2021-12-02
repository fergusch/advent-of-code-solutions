## advent of code 2019
## https://adventofcode.com/2019
## day 01

import math

def parse_input(lines):
    return [int(x) for x in lines]

def part1(data):
    return sum([math.floor(mass/3)-2 for mass in data])

def part2(data):
    total_fuel = 0
    for mass in data:
        fuel_needed = math.floor(mass/3)-2
        extra_weight = fuel_needed
        while True:
            extra_weight = math.floor(extra_weight/3)-2
            if extra_weight > 0:
                fuel_needed += extra_weight
            else:
                break
        total_fuel += fuel_needed
    return total_fuel