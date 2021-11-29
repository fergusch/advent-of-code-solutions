## advent of code 2020
## https://adventofcode.com/2020
## day 6

with open('input.txt', 'r') as f:
    forms = [x.replace('\n', ' ').strip() for x in f.read().split("\n\n")]

# part one ------------------------------------------------

total = 0
for form in forms:
    total += len(set(list(form.replace(' ', ''))))
print(total)

# part two ------------------------------------------------

total = 0
for form in forms:
    total += len(set.intersection(*[set(x) for x in form.split(' ')]))
print(total)