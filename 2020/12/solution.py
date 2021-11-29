## advent of code 2020
## https://adventofcode.com/2020
## day 12

with open('input.txt', 'r') as f:
    instructions = [(x[0], int(x[1:])) for x in f.readlines()]

dirs = {
    'N': {'values': (0, 1), 90: 'E', 180: 'S', 270: 'W'},
    'S': {'values': (0, -1), 90: 'W', 180: 'N', 270: 'E'},
    'E': {'values': (1, 0), 90: 'S', 180: 'W', 270: 'N'},
    'W': {'values': (-1, 0), 90: 'N', 180: 'E', 270: 'S'}
}

# part one ------------------------------------------------

x, y = 0, 0
dir = 'E'
for instr in instructions:

    if instr[0] in dirs:
        x += (dirs[instr[0]]['values'][0]*instr[1])
        y += (dirs[instr[0]]['values'][1]*instr[1])
    elif instr[0] == 'L':
        dir = dirs[dir][360-instr[1]]
    elif instr[0] == 'R':
        dir = dirs[dir][instr[1]]
    elif instr[0] == 'F':
        x += (instr[1]*dirs[dir]['values'][0])
        y += (instr[1]*dirs[dir]['values'][1])

print(abs(x)+abs(y))

# part two ------------------------------------------------

ship_x, ship_y, wp_x, wp_y = 0, 0, 10, 1
for instr in instructions:
    if instr[0] in dirs:
        wp_x += (dirs[instr[0]]['values'][0]*instr[1])
        wp_y += (dirs[instr[0]]['values'][1]*instr[1])
    elif instr[0] == 'L':
        if instr[1] == 90:
            wp_y *= -1
            wp_x, wp_y = wp_y, wp_x
        elif instr[1] == 180:
            wp_x *= -1; wp_y *= -1
        elif instr[1] == 270:
            wp_x *= -1
            wp_x, wp_y = wp_y, wp_x
    elif instr[0] == 'R':
        if instr[1] == 90:
            wp_x *= -1
            wp_x, wp_y = wp_y, wp_x
        elif instr[1] == 180:
            wp_x *= -1; wp_y *= -1
        elif instr[1] == 270:
            wp_y *= -1
            wp_x, wp_y = wp_y, wp_x
    elif instr[0] == 'F':
        ship_x += (wp_x*instr[1])
        ship_y += (wp_y*instr[1])

print(abs(ship_x)+abs(ship_y))