## advent of code 2021
## https://adventofcode.com/2021
## day 06

def parse_input(lines):
    return [int(x) for x in lines[0].strip().split(',')]

def part1(ages):
    N = 80
    for n in range(N):
        new_ages = ages.copy()
        for i, age in enumerate(ages):
            if age == 0:
                new_ages[i] = 6
                new_ages.append(8)
            else:
                new_ages[i] -= 1
        ages = new_ages.copy()
    return len(ages)

def part2(ages):
    N = 256
    age_counts = [0]*9
    for age in ages:
        age_counts[age] += 1
    for n in range(N):
        # adding the old values as a quick n dirty 
        # workaround to python passing references
        new_age_counts = [0]*9
        new_age_counts[6] += age_counts[0]
        new_age_counts[8] += age_counts[0]
        for i in range(8):
            new_age_counts[i] += age_counts[i+1]
        age_counts = new_age_counts.copy()
    return sum(age_counts)