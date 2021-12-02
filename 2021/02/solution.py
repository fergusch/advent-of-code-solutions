## advent of code 2021
## https://adventofcode.com/2021
## day 02

def parse_input(lines):
    return [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]

def part1(instructions):
    x, depth = 0, 0
    for instr in instructions:
        if instr[0] == 'forward':
            x += instr[1]
        elif instr[0] == 'down':
            depth += instr[1]
        elif instr[0] == 'up':
            depth -= instr[1]
    return x*depth

def part2(instructions):
    x, depth, aim = 0, 0, 0
    for instr in instructions:
        if instr[0] == 'forward':
            x += instr[1]
            depth += (aim*instr[1])
        elif instr[0] == 'down':
            aim += instr[1]
        elif instr[0] == 'up':
            aim -= instr[1]
    return x*depth