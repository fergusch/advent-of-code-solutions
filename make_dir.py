import sys
import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

cookies = {'session': os.environ['ADVENT_SESSION']}

year, day = sys.argv[1].split('/')
os.mkdir(f'{year}/{day}')

r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}', cookies=cookies)
soup = BeautifulSoup(r.text, 'html.parser')
part1_html = soup.find('article').decode_contents()
part1_html = re.sub('--- (.*) ---', r'\1', part1_html)
with open(f'{year}/{day}/prompt.md', 'w') as f:
    f.write(markdownify(part1_html).replace('\n\n', '\n'))

r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}/input', cookies=cookies)
with open(f'{year}/{day}/input.txt', 'w') as f:
    f.write(r.text)

with open(f'{year}/{day}/solution.py', 'w') as f:
    f.write(f'## advent of code {year}\n' + \
        f'## https://adventofcode.com/{year}\n' + \
        f'## day {day}\n\n' + \
        '# part one ------------------------------------------------\n\n' + \
        '# part two ------------------------------------------------')