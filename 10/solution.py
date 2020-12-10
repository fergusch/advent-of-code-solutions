## advent of code 2020
## https://adventofcode.com/2020
## day 10

with open('input.txt', 'r') as f:
    adapters = sorted([int(x) for x in f.readlines()])

# part one ------------------------------------------------

adapters = [0] + adapters + [max(adapters)+3]
counts = [0, 0, 0]

for i, num in enumerate(adapters):
    if i == 0: continue
    counts[adapters[i]-adapters[i-1]-1] += 1

print(counts[0]*counts[2])

# part two ------------------------------------------------

counts = [1] + ([0]*adapters[-1])

for i, num in enumerate(adapters):
    if i == 0: continue
    counts[num] = counts[num-3] + counts[num-2] + counts[num-1]

print(counts[-1])