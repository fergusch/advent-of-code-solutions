## advent of code 2020
## https://adventofcode.com/2020
## day 2

with open('input.txt', 'r') as f:
    passwords = [x.strip() for x in f.readlines()]

# part one ------------------------------------------------

valid_count = 0

for s in passwords:
    min, max = [int(x) for x in s.split(' ')[0].split('-')]
    req_char = s.split(': ')[0].split(' ')[1]
    password = s.split(': ')[1]
    
    count = 0
    for char in password:
        if char == req_char:
            count += 1

    if count >= min and count <= max:
        valid_count += 1

print(valid_count)

# part two ------------------------------------------------

valid_count = 0

for s in passwords:
    pos1, pos2 = [int(x)-1 for x in s.split(' ')[0].split('-')]
    req_char = s.split(': ')[0].split(' ')[1]
    password = s.split(': ')[1]

    if (password[pos1] == req_char and password[pos2] != req_char) \
        or (password[pos1] != req_char and password[pos2] == req_char):
        valid_count += 1

print(valid_count)