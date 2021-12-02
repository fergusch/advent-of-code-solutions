import sys
import os
import re
import requests
from importlib import import_module
from enum import Enum
from bs4 import BeautifulSoup
from markdownify import markdownify
from termcolor import colored
from tabulate import tabulate

class Status(Enum):
    PASS = 0
    FAIL = 1
    RATE_LIMIT = 2
    COMPLETED = 3
    UNKNOWN = 4

def compute_answers(year, day, file):

    solution = import_module(f'{year}.{day}.{file}')

    with open(f'{year}/{day}/input.txt', 'r') as f:
        data = solution.parse_input(f.readlines())
    if not isinstance(data, tuple):
        data = (data,)

    part1_answer = solution.part1(*data)
    part2_answer = solution.part2(*data)

    return part1_answer, part2_answer

def submit_answer(year, day, level, answer):
    payload = {'level': level, 'answer': answer}
    r = requests.post(f'https://adventofcode.com/{year}/day/{int(day)}/answer', data=payload, cookies=cookies)
    response = r.text
    if "That's the right answer" in response:
        print(colored('Correct!', 'green'), end=' ')
        if level == '1':
            print(colored('*', 'cyan'))
        elif level == '2':
            print(colored('**', 'yellow'))
        return Status.PASS
    elif "That's not the right answer" in response:
        print(colored('Incorrect!', 'red'))
        return Status.FAIL
    elif 'You gave an answer too recently' in response:
        print(colored('Rate limited! Please wait before submitting again.', 'yellow'))
        return Status.RATE_LIMIT
    elif 'Did you already complete it?' in response:
        print(colored("You've already completed this question.", 'yellow'))
        return Status.COMPLETED
    else:
        print(colored('Something went wrong. Please view the output below:', 'red'))
        print(response)
        return Status.UNKNOWN

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('usage:\n')
        print('  (dates are YYYY/DD format)\n')
        print(colored('  aoc.py get YEAR/DAY', 'magenta'))
        print('    create directory ./YEAR/DAY/, download input and part 1 prompt,')
        print('    and generate solution.py template\n')
        print(colored('  aoc.py dry YEAR/DAY [SOLUTION_FILE]', 'magenta'))
        print('    dry run: print solution.py output for YEAR/DAY without submitting')
        print('    - if SOLUTION_FILE is specified, print output of that file and')
        print('      compare to solution.py output.\n')
        print(colored('  aoc.py submit YEAR/DAY [SOLUTION_FILE]', 'magenta'))
        print('    run solution.py and submit answers for YEAR/DAY')
        print('    - if part 2 is unsolved, submit part 1 and append part 2 text to prompt file.')
        print('    - if both parts are solved, submit part 2.')
        print('    - if SOLUTION_FILE is specified and answers not yet submitted,')
        print('      submit answers using that file instead.\n')
        print(colored('  aoc.py stats YEAR', 'magenta'))
        print('    check progress and personal leaderboard stats for YEAR\n')
        sys.exit(0)

    command = sys.argv[1]
    year, day = sys.argv[2].split('/') if '/' in sys.argv[2] else (sys.argv[2], '')
    solution_file = 'solution' if len(sys.argv) < 4 else sys.argv[3]
    cookies = {'session': os.environ['ADVENT_SESSION']}

    if command == 'stats':

        r = requests.get(f'https://adventofcode.com/{year}/leaderboard/self', cookies=cookies)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.select('article pre')[0].text
        table_rows = [x.split() for x in table.split('\n')[2:-1]]
        stars_per_day = [0]*25
        for row in table_rows:
            stars_per_day[int(row[0])-1] = 2 if row[4:7] != ['-', '-', '-'] else 1 if row[1:4] != ['-', '-', '-'] else 0
        
        print()
        print(colored('(Part 1)', 'cyan'), colored('(Part 2)', 'yellow'))
        print('\n         1111111111222222\n1234567890123456789012345')
        for day in stars_per_day:
            print(colored('*', 'yellow') if day == 2 else colored('*', 'cyan') if day == 1 else ' ', end='')
        print(f" ({sum(stars_per_day)}{colored('*', 'yellow')})\n")

        print(tabulate(table_rows, headers=['Day', 
            *[colored(x, 'cyan') for x in ['Time', 'Rank', 'Score']],
            *[colored(x, 'yellow') for x in ['Time', 'Rank', 'Score']]
        ]), '\n')
    
    elif command == 'get':
        
        os.mkdir(f'{year}/{day}')

        r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}', cookies=cookies)
        soup = BeautifulSoup(r.text, 'html.parser')
        part1_html = soup.find('article', class_='day-desc').decode_contents()
        part1_html = re.sub('--- (.*) ---', r'\1', part1_html)
        with open(f'{year}/{day}/prompt.md', 'w') as f:
            f.write(markdownify(part1_html).replace('\n\n', '\n'))

        r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}/input', cookies=cookies)
        with open(f'{year}/{day}/input.txt', 'w') as f:
            f.write(r.text)

        with open(f'{year}/{day}/solution.py', 'w') as f:
            f.write(f'## advent of code {year}\n## https://adventofcode.com/{year}\n## day {day}\n\n' + \
                    'def parse_input(lines):\n    pass\n\n' + \
                    'def part1(data):\n    pass\n\n' + \
                    'def part2(data):\n    pass')

        print(f'Downloaded part 1 prompt to {year}/{day}/prompt.md')

    else:

        part1_answer, part2_answer = compute_answers(year, day, solution_file)

        if command == 'dry':

            print(part1_answer, part2_answer)

            if solution_file != 'solution':
                part1_orig_ans, part2_orig_ans = compute_answers(year, day, 'solution')
                if (part1_orig_ans, part2_orig_ans) == (part1_answer, part2_answer):
                    print(colored('Output matches solution.py', 'green'))
                else:
                    print(colored('Output does not match solution.py:', 'red'))
                    print(colored(part1_orig_ans, 'red'), colored(part2_orig_ans, 'red'))
            
            sys.exit(0)

        elif command == 'submit':

            if part2_answer is None:
                status = submit_answer(year, day, '1', part1_answer)
                if status == Status.PASS:
                    r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}', cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    part2_html = soup.find_all('article', class_='day-desc')[1].decode_contents()
                    part2_html = re.sub('--- (.*) ---', r'\1', part2_html)
                    with open(f'{year}/{day}/prompt.md', 'a') as f:
                        f.write(markdownify(part2_html).replace('\n\n', '\n'))
                        
                    print(f'Appended part 2 prompt to {year}/{day}/prompt.md')

            else:
                status = submit_answer(year, day, '2', part2_answer)
                if status == Status.PASS:
                    print(f'Day {int(day)} complete!')