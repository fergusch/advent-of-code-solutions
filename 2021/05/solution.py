## advent of code 2021
## https://adventofcode.com/2021
## day 05

def parse_input(lines):
    pairs = []
    for line in lines:
        p1, p2 = line.strip().split(' -> ')
        pairs.append((tuple(p1.split(',')), tuple(p2.split(','))))
    return pairs

def part1(pairs):
    graph = {}
    for pair in pairs:
        x1, y1, x2, y2 = int(pair[0][0]), int(pair[0][1]), int(pair[1][0]), int(pair[1][1])
        if x1 == x2:
            start, end = min(y1, y2), max(y1, y2)
            for i in range(int(start), int(end)+1):
                p = (x1, i)
                if p in graph:
                    graph[p] += 1
                else:
                    graph[p] = 1
        elif y1 == y2:
            start, end = min(x1, x2), max(x1, x2)
            for i in range(int(start), int(end)+1):
                p = (i, y1)
                if p in graph:
                    graph[p] += 1
                else:
                    graph[p] = 1

    return len([(p, graph[p]) for p in graph if graph[p]>1])

def part2(pairs):
    graph = {}
    for pair in pairs:
        x1, y1, x2, y2 = int(pair[0][0]), int(pair[0][1]), int(pair[1][0]), int(pair[1][1])
        if x1 == x2:
            start, end = min(y1, y2), max(y1, y2)
            for i in range(int(start), int(end)+1):
                p = (x1, i)
                if p in graph:
                    graph[p] += 1
                else:
                    graph[p] = 1
        elif y1 == y2:
            start, end = min(x1, x2), max(x1, x2)
            for i in range(int(start), int(end)+1):
                p = (i, y1)
                if p in graph:
                    graph[p] += 1
                else:
                    graph[p] = 1
        elif (y2 - y1) == (x1 - x2):
            x, y = x1, y1
            if x1 < x2:
                while x <= x2:
                    p = (x, y)
                    if p in graph:
                        graph[p] += 1
                    else:
                        graph[p] = 1
                    x += 1
                    y -= 1
            elif x1 > x2:
                while x >= x2:
                    p = (x, y)
                    if p in graph:
                        graph[p] += 1
                    else:
                        graph[p] = 1
                    x -= 1
                    y += 1
        elif (y2 - y1) == (x2 - x1):
            x, y = x1, y1
            if x1 < x2:
                while x <= x2:
                    p = (x, y)
                    if p in graph:
                        graph[p] += 1
                    else:
                        graph[p] = 1
                    x += 1
                    y += 1
            elif x1 > x2:
                while x >= x2:
                    p = (x, y)
                    if p in graph:
                        graph[p] += 1
                    else:
                        graph[p] = 1
                    x -= 1
                    y -= 1

    return len([(p, graph[p]) for p in graph if graph[p]>1])