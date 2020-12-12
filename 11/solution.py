## advent of code 2020
## https://adventofcode.com/2020
## day 11

from copy import deepcopy

with open('input.txt', 'r') as f:
    rows = [['.'] + list(x.strip()) + ['.'] for x in f.readlines()]

rows = list(['.'*len(rows[0])]) + rows + list(['.'*len(rows[0])])

def simulate(start_state, death_thresh=4):
    last_state = deepcopy(rows)
    while True:
        current_state = deepcopy(last_state)
        for i in range(1, len(rows)-1):
            for j in range(1, len(rows[0])-1):
                if last_state[i][j] == 'L' and \
                    adj_occupied(last_state, i, j) == 0:
                    current_state[i][j] = '#'
                elif last_state[i][j] == '#' and \
                    adj_occupied(last_state, i, j) >= death_thresh:
                    current_state[i][j] = 'L'
        if current_state == last_state:
            total = 0
            for i in range(1, len(current_state)-1):
                for j in range(1, len(current_state[0])-1):
                    if current_state[i][j] == '#':
                        total += 1
            print(total)
            break
        else:
            last_state = current_state

# part one ------------------------------------------------

def adj_occupied(state, i, j):
    occupied = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0: continue
            if state[i+k][j+l] == '#':
                occupied += 1
    return occupied

simulate(rows)

# part two ------------------------------------------------

def adj_occupied(state, i, j):
    occupied = 0

    # vertical
    for k in range(1, i+1):
        if state[i-k][j] != '.':
            occupied += 1 if state[i-k][j] == '#' else 0; break
    for k in range(1, len(state)-i):
        if state[i+k][j] != '.':
            occupied += 1 if state[i+k][j] == '#' else 0; break

    # horizontal
    for k in range(1, j+1):
        if state[i][j-k] != '.':
            occupied += 1 if state[i][j-k] == '#' else 0; break
    for k in range(1, len(state[0])-j):
        if state[i][j+k] != '.':
            occupied += 1 if state[i][j+k] == '#' else 0; break

    # \ diagonal
    for k in range(1, min(i, j)+1):
        if state[i-k][j-k] != '.':
            occupied += 1 if state[i-k][j-k] == '#' else 0; break
    for k in range(1, min(len(state)-i, len(state[0])-j)):
        if state[i+k][j+k] != '.':
            occupied += 1 if state[i+k][j+k] == '#' else 0; break

    # / diagonal
    for k in range(1, min(len(state)-i, j)):
        if state[i+k][j-k] != '.':
            occupied += 1 if state[i+k][j-k] == '#' else 0; break
    for k in range(1, min(i, len(state[0])-j)):
        if state[i-k][j+k] != '.':
            occupied += 1 if state[i-k][j+k] == '#' else 0; break

    return occupied

simulate(rows, death_thresh=5)
