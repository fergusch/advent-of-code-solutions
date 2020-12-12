import pygame, pygame.freetype
import random
import os
from copy import deepcopy

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((400, 368))
pygame.display.set_caption("Advent of Code 2020 - Day 11")
clock = pygame.time.Clock()

with open('input.txt', 'r') as f:
    rows = [['.'] + list(x.strip()) + ['.'] for x in f.readlines()]
rows = list(['.'*len(rows[0])]) + rows + list(['.'*len(rows[0])])

def adj_occupied(state, i, j):
    occupied = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0: continue
            if state[i+k][j+l] == '#':
                occupied += 1
    return occupied

all_states = [rows]

def simulate(start_state, death_thresh=4):
    last_state = deepcopy(rows)
    while True:
        all_states.append(last_state)
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
            break
        else:
            last_state = current_state

simulate(rows)

running = True
state_num = 0
while running:

    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in range(len(all_states[state_num])):
        for j in range(len(all_states[state_num][0])):
            if all_states[state_num][i][j] == '#' \
                and adj_occupied(all_states[state_num], i, j) < 4:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i*4, j*4, 4, 4))
            elif all_states[state_num][i][j] == 'L' \
                and adj_occupied(all_states[state_num], i, j) > 0:
                pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(i*4, j*4, 4, 4))

    pygame.display.flip()

    state_num += 1
    if state_num >= len(all_states): running = False

pygame.quit()
