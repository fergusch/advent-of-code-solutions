## advent of code 2021
## https://adventofcode.com/2021
## day 14

from collections import Counter, defaultdict
import re
from math import ceil

def parse_input(lines):
    template = lines[0]
    rules = {re.findall('([A-Z]{2}) ->', s)[0]: re.findall('-> ([A-Z]{1})', s)[0] for s in lines[1:]}
    return template, rules

def part1(template, rules):
    t = template
    for n in range(10):
        s = t[:1]
        for i in range(len(t)-1):
            pair = f'{t[i]}{t[i+1]}'
            if pair in rules:
                s += f'{rules[pair]}{t[i+1]}'
        t = s
    counts = Counter(t).most_common()
    return counts[0][1] - counts[-1][1]

def part2(template, rules):
    counts = defaultdict(int)
    for i in range(len(template)-1):
        counts[f'{template[i]}{template[i+1]}'] += 1
    t = template
    for n in range(40):
        new_counts = defaultdict(int)
        for pair in counts:
            if pair in rules:
                new_str = f'{pair[0]}{rules[pair]}{pair[1]}'
                new_counts[new_str[:2]] += counts[pair]
                new_counts[new_str[1:]] += counts[pair]
        counts = new_counts.copy()
    letters = defaultdict(int)
    for pair in counts:
        # divide by 2 since each letter appears in two pairs
        letters[pair[0]] += counts[pair]/2
        letters[pair[1]] += counts[pair]/2
    letters = [(k, ceil(v)) for k, v in sorted(letters.items(), reverse=True, key=lambda x: x[1])]
    return letters[0][1] - letters[-1][1]