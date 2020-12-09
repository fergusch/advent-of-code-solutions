## advent of code 2020
## https://adventofcode.com/2020
## day 7

with open('input.txt', 'r') as f:
    rules = [x.strip().replace('.', '') for x in f.readlines()]

count_dict = {}

for rule in rules:
    outer = rule.split(' contain ')[0].replace(' bags', '')
    inner = [(' '.join(x.split(' ')[1:3]), int(x.split(' ')[0])) for x in rule.split(' contain ')[1].split(', ')] \
                if rule.split(' contain ')[1] != 'no other bags' else []

    count_dict[outer] = inner

# part one ------------------------------------------------

def can_contain(outer, inner):
    if not count_dict[outer]:
        return False
    if inner in [t[0] for t in count_dict[outer]]:
        return True
    for color in [t[0] for t in count_dict[outer]]:
        if can_contain(color, inner):
            return True
    return False

count = 0
for color in count_dict:
    if can_contain(color, 'shiny gold'):
        count += 1

print(count)

# part two ------------------------------------------------

def must_contain(color):
    if not count_dict[color]:
        return 0
    count = 0
    for c in count_dict[color]:
        count += c[1]
        count += must_contain(c[0])*c[1]
    return count

print(must_contain('shiny gold'))