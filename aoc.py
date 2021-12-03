import sys
import os
import re
import requests
from importlib import import_module
from datetime import datetime as dt
from enum import Enum
from bs4 import BeautifulSoup
from markdownify import markdownify
from termcolor import colored as termcolor_colored
from tabulate import tabulate
import pytz

class Status(Enum):
    PASS = 0
    FAIL = 1
    RATE_LIMIT = 2
    COMPLETED = 3
    UNKNOWN = 4

def colored(text, color):
    if 'ADVENT_DISABLE_TERMCOLOR' in os.environ and os.environ['ADVENT_DISABLE_TERMCOLOR'] == '1':
        if text == '*':
            if color == 'cyan':
                return '/'
            elif color == 'grey':
                return '.'
        return text
    else:
        return termcolor_colored(text, color)

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
        print('\nusage:\n')
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
        print(colored('  aoc.py stats YEAR [private]', 'magenta'))
        print('    check progress and personal leaderboard stats for YEAR')
        print('    - if "private" passed, show configured private leaderboard stats.\n')
        print('configuration environment variables:\n')
        print(' ', colored('ADVENT_SESSION', 'magenta'), '          : AoC session cookie', colored('(required)', 'red'))
        print(' ', colored('ADVENT_PRIV_BOARDS', 'magenta'), '      : comma-separated list of private leaderboard IDs')
        print(' ', colored('ADVENT_DISABLE_TERMCOLOR', 'magenta'), ': set to "1" to disable coloring terminal output\n')
        sys.exit(0)

    command = sys.argv[1]
    year, day = sys.argv[2].split('/') if '/' in sys.argv[2] else (sys.argv[2], '')
    solution_file = 'solution' if len(sys.argv) < 4 else sys.argv[3]
    cookies = {'session': os.environ['ADVENT_SESSION']}
    private_leaderboards = []

    if command == 'stats':

        # I know this is a bad way to do this, but isn't that the fun of this whole thing?
        if solution_file == 'private':

            if 'ADVENT_PRIV_BOARDS' in os.environ:
                private_leaderboards = os.environ['ADVENT_PRIV_BOARDS'].split(',')
            else:
                print(colored('You are not a member of any private leaderboards.', 'red'))

            for board_id in private_leaderboards:

                r = requests.get(f'https://adventofcode.com/{year}/leaderboard/private/view/{board_id}', cookies=cookies)
                soup = BeautifulSoup(r.text, 'html.parser')
                board_owner = re.findall(r'private leaderboard of (.*) for', soup.select('article p')[0].text)[0]
                rows = soup.find_all('div', class_='privboard-row')[1:]

                top_score_len = len(rows[0].find_all(text=True, recursive=False)[0].strip())
                print(f"\n{board_owner}'s private leaderboard {colored(f'({board_id})', 'grey')}")
                print(f'\n{" "*(top_score_len+14)}1111111111222222\n{" "*(top_score_len+5)}1234567890123456789012345')

                for i, row in enumerate(rows):
                    position = row.find('span', class_='privboard-position').text
                    stars = row.find_all('span', class_=re.compile('privboard-star-*'))
                    name = row.find('span', class_='privboard-name').text
                    name_link = row.select('.privboard-name a')[0].attrs['href'] if len(row.select('.privboard-name a')) else None
                    score = row.find_all(text=True, recursive=False)[0].strip()

                    print(f'{position} {score:>{top_score_len}}', end=' ')
                    for i, span in enumerate(stars):
                        class_ = span.attrs['class'][0]
                        if 'both' in class_: 
                            print(colored('*', 'yellow'), end='')
                        elif 'firstonly' in class_:
                            print(colored('*', 'cyan'), end='')
                        elif 'unlocked' in class_:
                            print(colored('*', 'grey'), end='')
                        elif 'locked' in class_:
                            print(' ', end='')
                    
                    print(f' {name}', end=' ')
                    print(f'({colored(name_link, "blue")})' if name_link is not None else '')
                
                print()
                print(f'({colored("*", "yellow")} 2 stars) ({colored("*", "cyan")} 1 star) ({colored("*", "grey")} 0 stars)\n')
                

        else:

            r = requests.get(f'https://adventofcode.com/{year}/leaderboard/self', cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            table = soup.select('article pre')[0].text
            table_rows = [x.split() for x in table.split('\n')[2:-1]]
            stars_per_day = [0]*25
            for row in table_rows:
                stars_per_day[int(row[0])-1] = 2 if row[4:7] != ['-', '-', '-'] else 1 if row[1:4] != ['-', '-', '-'] else 0

            print('\n         1111111111222222\n1234567890123456789012345')
            for i, stars in enumerate(stars_per_day):
                today = dt.now(pytz.timezone('America/New_York'))
                if stars == 2:
                    print(colored('*', 'yellow'), end='')
                elif stars == 1:
                    print(colored('*', 'cyan'), end='')
                elif stars == 0 and today.year == int(year) and today.day < i+1:
                    print(' ', end='')
                else:
                    print(colored('*', 'grey'), end='')

            print(f" ({sum(stars_per_day)}{colored('*', 'yellow')})\n")
            print(f'({colored("*", "yellow")} 2 stars) ({colored("*", "cyan")} 1 star) ({colored("*", "grey")} 0 stars)\n')

            print(tabulate(table_rows, stralign='right', headers=['\nDay', 
                *['\n'.join([colored(y, 'cyan') for y in x.split('\n')]) for x in ['----\nTime', '(Part 1)\nRank', '----\nScore']],
                *['\n'.join([colored(y, 'yellow') for y in x.split('\n')]) for x in ['----\nTime', '(Part 2)\nRank', '----\nScore']]
            ]), '\n')

            if 'ADVENT_PRIV_BOARDS' in os.environ:
                private_leaderboards = os.environ['ADVENT_PRIV_BOARDS'].split(',')
            else:
                sys.exit(0)

            print(colored(f'You are a member of {len(private_leaderboards)} private leaderboard(s).', 'grey'))
            print(colored(f'Use "aoc.py stats {year} private" to see them.\n', 'grey'))
    
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