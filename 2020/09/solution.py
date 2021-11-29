## advent of code 2020
## https://adventofcode.com/2020
## day 9

with open('input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

# part one ------------------------------------------------

invalid_num = 0
for i, num in enumerate(numbers):
    if i < 25: continue
    meets_condition = False
    for j in numbers[i-25:i]:
        for k in numbers[i-25:i]:
            if j == k: break
            elif j+k == num:
                meets_condition = True
                break
    if not meets_condition:
        invalid_num = num; print(num)
        break

# part two ------------------------------------------------

for i in range(2, len(numbers)+1):
    for j in range(len(numbers)-i):
        if sum(numbers[j:j+i]) == invalid_num:
            print(min(numbers[j:j+i]) + max(numbers[j:j+i]))
            exit()