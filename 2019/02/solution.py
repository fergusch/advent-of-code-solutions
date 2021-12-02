## advent of code 2019
## https://adventofcode.com/2019
## day 02

def parse_input(lines):
    return [int(x) for x in lines[0].split(',')]

def run_intcode(p, noun, verb):
    program = p.copy()
    program[1] = noun
    program[2] = verb
    i = 0
    while program[i] != 99:
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        i += 4
    return program[0]

def part1(program):
    return run_intcode(program, 12, 2)

def part2(program):
    for noun in range(100):
        for verb in range(100):
            if run_intcode(program, noun, verb) == 19690720:
                return 100 * noun + verb