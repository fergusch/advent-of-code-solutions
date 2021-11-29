## advent of code 2020
## https://adventofcode.com/2020
## day 5

with open('input.txt', 'r') as f:
    passes = f.readlines()

# part one ------------------------------------------------

max_id = 0
for p in passes:
    id = int(p.replace('F', '0')
              .replace('B', '1')
              .replace('L', '0')
              .replace('R', '1'), 2)
    if id > max_id: max_id = id
print(max_id)

# part two ------------------------------------------------

ids = []
for p in passes:
    id = int(p.replace('F', '0')
              .replace('B', '1')
              .replace('L', '0')
              .replace('R', '1'), 2)
    ids.append(id)
print((set(ids) ^ set(range(sorted(ids)[0], sorted(ids)[-1]+1))).pop())