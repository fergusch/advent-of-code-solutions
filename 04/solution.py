## advent of code 2020
## https://adventofcode.com/2020
## day 4

import re

with open('input.txt', 'r') as f:
    passports = [x.replace('\n', ' ').strip() for x in f.read().split("\n\n")]

# part one ------------------------------------------------

valid_count = 0

for passport in passports:
    valid_count = valid_count + 1 \
        if re.match(r'^(?=.*\bbyr:)(?=.*\biyr:)(?=.*\beyr:)'
                    r'(?=.*\bhgt:)(?=.*\bhcl:)(?=.*\becl:)'
                    r'(?=.*\bpid:).*$', passport) \
        else valid_count

print(valid_count)

# part two ------------------------------------------------

valid_count = 0

for passport in passports:
    valid_count = valid_count + 1 \
        if re.match(r'^(?=.*\bbyr:(19[2-9][0-9]|200[0-2])\b)'
                    r'(?=.*\biyr:(201[0-9]|2020)\b)'
                    r'(?=.*\beyr:(202[0-9]|2030)\b)'
                    r'(?=.*\bhgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)\b)'
                    r'(?=.*\bhcl:#[a-f0-9]{6}\b)'
                    r'(?=.*\becl:(amb|blu|brn|gry|grn|hzl|oth)\b)'
                    r'(?=.*\bpid:[0-9]{9}\b).*$', passport) \
        else valid_count

print(valid_count)