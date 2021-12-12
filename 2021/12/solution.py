## advent of code 2021
## https://adventofcode.com/2021
## day 12

from collections import defaultdict

def parse_input(lines):
    graph = defaultdict(list)
    for line in lines:
        u, v = line.split('-')
        graph[u].append(v)
        graph[v].append(u)
    return graph

def part1(graph):
    visited = set()
    stack = []
    paths = []

    def dfs(u):
        if u.islower():
            visited.add(u)
        stack.append(u)
        if u == 'end':
            paths.append(stack.copy())
        else:
            for v in graph[u]:
                if v not in visited:
                    dfs(v)
        stack.pop()
        if u in visited:
            visited.remove(u)

    dfs('start')
    return len(paths)

def part2(graph):
    visited = {k: 0 for k in graph.keys() if k.islower()}
    stack = []
    paths = []

    def dfs(u):
        if u.islower():
            if visited[u] == 1 and (u in ['start', 'end'] or 2 in visited.values()):
                return
            else:
                visited[u] += 1
        stack.append(u)
        if u == 'end':
            paths.append(stack.copy())
        else:
            for v in graph[u]:
                if v.isupper() or visited[v] < 2:
                    dfs(v)
        stack.pop()
        if u in visited:
            visited[u] -= 1

    dfs('start')
    return len(paths)