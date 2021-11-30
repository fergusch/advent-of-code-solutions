import sys
import os

year, day = sys.argv[1].split('/')
os.mkdir(f'{year}/{day}')
open(f'{year}/{day}/input.txt', 'w').close()
with open(f'{year}/{day}/solution.py', 'w') as f:
    f.write(f'## advent of code {year}\n' + \
        f'## https://adventofcode.com/{year}\n' + \
        f'## day {day}\n\n' + \
        '# part one ------------------------------------------------\n\n' + \
        '# part two ------------------------------------------------')