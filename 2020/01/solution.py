## advent of code 2020
## https://adventofcode.com/2020
## day 1

with open('input.txt', 'r') as f:
    expenses = sorted([int(x.strip()) for x in f.readlines()])

# part one ------------------------------------------------

for item in expenses:
    if 2020 - item not in expenses:
        continue
    else:
        print(item * (2020 - item))
        break

# part two ------------------------------------------------

for item_1 in expenses:
    for item_2 in expenses:
        if 2020 - item_1 - item_2 not in expenses:
            continue
        else:
            print(item_1 * item_2 * (2020 - item_1 - item_2))
            exit()