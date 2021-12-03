## advent of code 2021
## https://adventofcode.com/2021
## day 03

def parse_input(lines):
    return [x.strip() for x in lines]

def part1(data):
    gamma = ['0']*12
    epsilon = ['1']*12
    for i in range(12):
        bits = [byte[i] for byte in data]
        if len([bit for bit in bits if bit == '0']) > len([bit for bit in bits if bit == '1']):
            gamma[i] = '0'
            epsilon[i] = '1'
        else:
            gamma[i] = '1'
            epsilon[i] = '0'
    return int(''.join(gamma),2) * int(''.join(epsilon),2)

def part2(data):
    oxygen = data.copy()
    for i in range(12):
        bits = [byte[i] for byte in oxygen]
        most_common = '0'
        if len([bit for bit in bits if bit == '1']) >= len([bit for bit in bits if bit == '0']):
            most_common = '1'
        to_delete = []
        for j in range(len(oxygen)):
            if not oxygen[j][i] != most_common:
                to_delete.append(j)
        oxygen = [oxygen[i] for i in range(len(oxygen)) if i not in to_delete]
        if len(oxygen) == 1:
            break

    co2 = data.copy()
    for i in range(12):
        bits = [byte[i] for byte in co2]
        least_common = '1'
        if len([bit for bit in bits if bit == '1']) >= len([bit for bit in bits if bit == '0']):
            least_common = '0'
        to_delete = []
        for j in range(len(co2)):
            if not co2[j][i] != least_common:
                to_delete.append(j)
        co2 = [co2[i] for i in range(len(co2)) if i not in to_delete]
        if len(co2) == 1:
            break

    return int(oxygen[0],2) * int(co2[0],2)
