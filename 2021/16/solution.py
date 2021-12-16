## advent of code 2021
## https://adventofcode.com/2021
## day 16

from functools import reduce

def parse_input(lines):
    return lines[0]

def hex2bin(hex_num):
    b = bin(int(hex_num, 16))[2:]
    while len(b) % 4 != 0:
        b = '0' + b
    return b

def part1(packet):
    
    def sum_versions(binary):
        if not binary:
            return 0, ''
        version = int(binary[:3], 2)
        type_id = int(binary[3:6], 2)
        if type_id == 4:
            i = 6
            while binary[i] == '1':
                i += 5
            i += 5
            return version, binary[i:]
        else:
            versions = [version]
            leftover = ''
            if binary[6] == '0':
                len_sub_packets = int(binary[7:22], 2)
                remaining = binary[22:22+len_sub_packets]
                while len(remaining) > 0:
                    v, r = sum_versions(remaining)
                    versions.append(v)
                    remaining = r
                leftover = binary[22+len_sub_packets:]
            elif binary[6] == '1':
                num_sub_packets = int(binary[7:18], 2)
                remaining = binary[18:]
                while num_sub_packets > 0:
                    v, r = sum_versions(remaining)
                    versions.append(v)
                    remaining = r
                    num_sub_packets -= 1
                leftover = remaining
            return sum(versions), leftover

    return sum_versions(hex2bin(packet))[0]

def part2(packet):
    
    def eval_packet(binary):
        if len(binary) < 6:
            return None, ''
        version = int(binary[:3], 2)
        type_id = int(binary[3:6], 2)
        if type_id == 4:
            i = 6
            number = ''
            while binary[i] == '1':
                number += binary[i+1:i+5]
                i += 5
            number += binary[i+1:i+5]
            i += 5
            return int(number, 2), binary[i:]
        else:
            values = []
            leftover = ''
            if binary[6] == '0':
                len_sub_packets = int(binary[7:22], 2)
                remaining = binary[22:22+len_sub_packets]
                while len(remaining) > 0:
                    v, r = eval_packet(remaining)
                    if v is not None:
                        values.append(v)
                    remaining = r
                leftover = binary[22+len_sub_packets:]
            elif binary[6] == '1':
                num_sub_packets = int(binary[7:18], 2)
                remaining = binary[18:]
                while num_sub_packets > 0:
                    v, r = eval_packet(remaining)
                    if v is not None:
                        values.append(v)
                    remaining = r
                    num_sub_packets -= 1
                leftover = remaining

            if type_id == 0:
                return sum(values), leftover
            elif type_id == 1:
                return reduce(lambda x, y: x*y, values), leftover
            elif type_id == 2:
                return min(values), leftover
            elif type_id == 3:
                return max(values), leftover
            elif type_id == 5:
                return int(values[0] > values[1]), leftover
            elif type_id == 6:
                return int(values[0] < values[1]), leftover
            elif type_id == 7:
                return int(values[0] == values[1]), leftover

    return eval_packet(hex2bin(packet))[0]
