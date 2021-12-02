import sys
import os
import re
import requests
from importlib import import_module
from enum import Enum
from bs4 import BeautifulSoup
from markdownify import markdownify
from termcolor import colored

class Status(Enum):
    PASS = 0
    FAIL = 1
    RATE_LIMIT = 2
    COMPLETED = 3
    UNKNOWN = 4

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
        print('usage: python aoc.py <command> <year>/<day-zero-padded>')
        print('commands:')
        print('  - get: download input and part 1 prompt to directory <year>/<day>')
        print('  - dry: dry-run; prints out answers without submitting')
        print('  - submit: submits the last unsubmitted answer, downloads part 2 prompt if not completed')
        sys.exit(0)

    command = sys.argv[1]
    year, day = sys.argv[2].split('/')
    cookies = {'session': os.environ['ADVENT_SESSION']}

    if command == 'get':
        
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

        print('Downloaded part 1 prompt.')

    else:

        solution = import_module(f'{year}.{day}.solution')

        with open(f'{year}/{day}/input.txt', 'r') as f:
            data = solution.parse_input(f.readlines())
        if not isinstance(data, tuple):
            data = (data,)

        part1_answer = solution.part1(*data)
        part2_answer = solution.part2(*data)

        if command == 'dry':
            print(part1_answer, part2_answer)
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
                        
                    print('Downloaded part 2 prompt.')

            else:
                status = submit_answer(year, day, '2', part2_answer)
                if status == Status.PASS:
                    print(f'Day {int(day)} complete!')