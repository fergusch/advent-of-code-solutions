## advent of code 2019
## https://adventofcode.com/2019
## day 03

def parse_input(lines):
    first_wire = [(x[0], int(x[1:])) for x in lines[0].strip().split(',')]
    second_wire = [(x[0], int(x[1:])) for x in lines[1].strip().split(',')]
    return first_wire, second_wire

def part1(first_wire, second_wire):
    first_wire_graph = set()
    intersections = []
    p = (0, 0)

    for instr in first_wire:
        if instr[0] in ['L', 'R']:
            new_x = p[0] + instr[1]*(-1 if instr[0] == 'L' else 1)
            for i in range(min(p[0], new_x), max(p[0], new_x)+1):
                first_wire_graph.add((i, p[1]))
            p = (new_x, p[1])
        elif instr[0] in ['U', 'D']:
            new_y = p[1] + instr[1]*(-1 if instr[0] == 'D' else 1)
            for i in range(min(p[1], new_y), max(p[1], new_y)+1):
                first_wire_graph.add((p[0], i))
            p = (p[0], new_y)
    p = (0, 0)
    for instr in second_wire:
        if instr[0] in ['L', 'R']:
            new_x = p[0] + instr[1]*(-1 if instr[0] == 'L' else 1)
            for i in range(min(p[0], new_x), max(p[0], new_x)+1):
                if (i, p[1]) in first_wire_graph:
                    intersections.append((i, p[1]))
            p = (new_x, p[1])
        elif instr[0] in ['U', 'D']:
            new_y = p[1] + instr[1]*(-1 if instr[0] == 'D' else 1)
            for i in range(min(p[1], new_y), max(p[1], new_y)+1):
                if (p[0], i) in first_wire_graph:
                    intersections.append((p[0], i))
            p = (p[0], new_y)
    
    closest_point = (float('inf'), float('inf'))
    min_dist = float('inf')
    for point in intersections:
        dist_to_origin = abs(point[0]) + abs(point[1])
        if 0 < dist_to_origin < min_dist:
            min_dist = dist_to_origin
            closest_point = point

    return min_dist

def part2(first_wire, second_wire):
    pass