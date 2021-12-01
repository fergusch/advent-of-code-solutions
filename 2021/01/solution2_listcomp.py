## advent of code 2021
## https://adventofcode.com/2021
## day 01
## ALT: using only list comprehensions

with open('input.txt', 'r') as f:
    depths = [int(x) for x in f.readlines()]

# part one ------------------------------------------------

print(sum([depths[i] > depths[i-1] for i in range(1, len(depths))]))

# part two ------------------------------------------------

print(sum([sum(depths[i-2:i+1]) > sum(depths[i-3:i]) for i in range(3, len(depths))]))