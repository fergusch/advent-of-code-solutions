## advent of code 2020
## https://adventofcode.com/2020
## day 14

import re
from copy import deepcopy

with open('input.txt', 'r') as f:
    instructions = [x.strip() for x in f.readlines()]

# part one ------------------------------------------------

mask = ''
mem = {}
for instr in instructions:
    if instr.startswith('mask ='):
        mask = instr.split(' = ')[1]
    else:
        r = re.search(r'^mem\[(\d+)\] = (\d+)$', instr)
        pos = int(r.group(1)); val = int(r.group(2))
        val_bin = list('{0:036b}'.format(val))
        for i, char in enumerate(mask):
            if char != 'X':
                val_bin[i] = char
        val = int(''.join(val_bin), 2)
        mem[pos] = val

print(sum(mem.values()))

# part two ------------------------------------------------

mask = ''
mem = {}
for instr in instructions:
    if instr.startswith('mask ='):
        mask = instr.split(' = ')[1]
    else:
        r = re.search(r'^mem\[(\d+)\] = (\d+)$', instr)
        pos_bin = list('{0:036b}'.format(int(r.group(1))))
        for i, char in enumerate(mask):
            if char == '1':
                pos_bin[i] = '1'
        addresses = []
        for i in range(2 ** mask.count('X')):
            bin = list('{0:0{1}b}'.format(i, mask.count('X')))
            masked_address = deepcopy(pos_bin)
            for j, pos in enumerate([x.start() for x in re.finditer('X', mask)]):
                masked_address[pos] = bin[j]
            mem[int(''.join(masked_address), 2)] = int(r.group(2))
        
print(sum(mem.values()))
