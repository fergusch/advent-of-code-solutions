## advent of code 2021
## https://adventofcode.com/2021
## day 10

def parse_input(lines):
    return lines

reversed = {
    '(': ')', 
    '[': ']', 
    '{': '}',  
    '<': '>', 
}
corrupt = []

def part1(data):
    total_score = 0
    for i, line in enumerate(data):
        stack = []
        for char in line:
            if not stack or char in reversed:
                stack.append(char)
            elif char not in reversed and char == reversed[stack[-1]]:
                stack.pop()
            else:
                total_score += {')': 3, ']': 57, '}': 1197, '>': 25137}[char]
                corrupt.append(i)
                break
    return total_score

def part2(data):
    data = [line for i, line in enumerate(data) if i not in corrupt]
    scores = []
    for line in data:
        stack = []
        completion_str = ''
        score = 0
        for i, char in enumerate(line):
            if not stack or char in reversed:
                stack.append(char)
            elif char not in reversed and char == reversed[stack[-1]]:
                stack.pop()
            elif i == len(line)-1:
                stack.append(char)
                break
        while stack:
            completion_str += reversed[stack[-1]]
            score = (score*5) + {')': 1, ']': 2, '}': 3, '>': 4}[reversed[stack[-1]]]
            stack.pop()
        scores.append(score)
    return sorted(scores)[(len(scores)//2)]
