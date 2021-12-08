## advent of code 2021
## https://adventofcode.com/2021
## day 08

from itertools import permutations
from tqdm import tqdm

def parse_input(lines):
    signals = [line.split(' | ')[0] for line in lines]
    digits = [line.split(' | ')[1] for line in lines]
    return signals, digits

def part1(signals, digits):
    return sum([len(d) in [2, 3, 4, 7] for i in range(len(digits)) for d in digits[i].split(' ')])

def part2(signals, digits):
    
    def convert_signal(signal, config):
        letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
        return ''.join(sorted([config[letters[x]] for x in list(signal)]))
    
    def validate_signal(signal):
        valid_digits = {
            'abcefg': '0',
            'cf': '1',
            'acdeg': '2',
            'acdfg': '3',
            'bcdf': '4',
            'abdfg': '5',
            'abdefg': '6',
            'acf': '7',
            'abcdefg': '8',
            'abcdfg': '9',
        }
        sorted_signal = ''.join(sorted(signal))
        if sorted_signal in valid_digits:
            return valid_digits[sorted_signal]
        else:
            return None
    
    total = 0
    for i in tqdm(range(len(signals))):
        for config in list(permutations('abcdefg')):
            converted_sigs = [convert_signal(s, config) for s in signals[i].split(' ')]
            if all([validate_signal(s) is not None for s in converted_sigs]):
                # this mapping is correct, calculate the number
                output = int(''.join([validate_signal(convert_signal(d, config)) for d in digits[i].split(' ')]))
                total += output
                break
    
    return total
