## advent of code 2020
## https://adventofcode.com/2020
## day 8

with open('input.txt', 'r') as f:
    instructions = [(x.split(' ')[0], int(x.split(' ')[1])) for x in f.readlines()]

# part one ------------------------------------------------

def run_instructions(instr):

    accumulator = 0
    current_step = 0
    logs = []

    while True:

        if current_step in logs:
            return False, accumulator
        elif current_step >= len(instr):
            return True, accumulator

        instruction = instr[current_step]
        if instruction[0] == 'acc':
            accumulator += instruction[1]
        elif instruction[0] == 'jmp':
            current_step += instruction[1]
            continue
        
        logs.append(current_step)
        current_step += 1

print(run_instructions(instructions)[1])

# part two ------------------------------------------------

instr_sets = []
for i, instruction in enumerate(instructions):
    mod_instr = instructions.copy()
    if instruction[0] == 'jmp':
        mod_instr[i] = ('nop', instruction[1])
    elif instruction[0] == 'nop':
        mod_instr[i] = ('jmp', instruction[1])
    instr_sets.append(mod_instr)

for iset in instr_sets:
    result = run_instructions(iset)
    if result[0]:
        print(result[1])
        break