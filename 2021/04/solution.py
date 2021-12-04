## advent of code 2021
## https://adventofcode.com/2021
## day 04

# bingos bonted?

from itertools import chain

def parse_input(lines):
    numbers = [x.strip() for x in lines[0].split(',')]
    boards = []
    i = 1
    while i < len(lines):
        boards.append([line.split() for line in lines[i+1:i+6]])
        i += 6
    return numbers, boards

def check_win(board):
    for i in range(5):
        if board[i] == ['x']*5 or [board[j][i] for j in range(5)] == ['x']*5:
            return True
    return False

def part1(numbers, boards):
    for num in numbers:
        for i, board in enumerate(boards):
            for j in range(5):
                for k in range(5):
                    if board[j][k] == num:
                        boards[i][j][k] = 'x'
                        if check_win(boards[i]):
                            return sum([int(n) for n in chain.from_iterable(boards[i]) if n != 'x'])*int(num)

def part2(numbers, boards):
    winning_boards = set()
    for num in numbers:
        for i, board in enumerate(boards):
            if i in winning_boards: continue
            for j in range(5):
                for k in range(5):
                    if boards[i][j][k] == num:
                        boards[i][j][k] = 'x'
                        if check_win(boards[i]):
                            if len(winning_boards) == (len(boards)-1):
                                return sum([int(n) for n in chain.from_iterable(boards[i]) if n != 'x'])*int(num)
                            else:
                                winning_boards.add(i)