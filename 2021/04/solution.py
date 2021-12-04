## advent of code 2021
## https://adventofcode.com/2021
## day 04

# bingos bonted? 👽

import numpy as np

def parse_input(lines):
    numbers = [int(x.strip()) for x in lines[0].split(',')]
    boards = []
    i = 2
    while i <= len(lines):
        boards.append([int(x) for x in ' '.join([line.strip() for line in lines[i:i+5]]).split()])
        i += 6
    return np.array(numbers), np.array(boards)

def check_win(board):
    board_matrix = np.reshape(board, (5, 5))
    return np.any([[np.isnan(board_matrix[i]).all() for i in range(5)],
                  [np.isnan(board_matrix.transpose()[i]).all() for i in range(5)]])

def part1(numbers, boards):
    for num in numbers:
        boards = np.where(boards == num, np.nan, boards)
        board_states = np.array([check_win(board) for board in boards])
        if np.any(board_states):
            return int(np.nansum(boards[np.argmax(board_states)])*num)


def part2(numbers, boards):
    last = -1
    for num in numbers:
        boards = np.where(boards == num, np.nan, boards)
        board_states = np.array([check_win(board) for board in boards])
        if np.count_nonzero(~board_states) == 1:
            last = np.argmin(board_states)
        if last > -1:
            if board_states[last]:
                return int(np.nansum(boards[last])*num)