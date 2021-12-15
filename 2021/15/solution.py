## advent of code 2021
## https://adventofcode.com/2021
## day 15

from collections import defaultdict
import numpy as np
from tqdm import tqdm
from pqdict import minpq # this supports updating priority which the builtin libraries do not

def parse_input(lines):
    return np.array([[int(x) for x in list(line)] for line in lines])

def get_neighbors(arr, y, x):
    neighbors = []
    if x > 0:
        neighbors.append((y, x-1))
    if x < len(arr[0])-1:
        neighbors.append((y, x+1))
    if y > 0:
        neighbors.append((y-1, x))
    if y < len(arr)-1:
        neighbors.append((y+1, x))
    return neighbors

def part1(graph):
    
    def dijkstra(graph, source, target):

        q = set()
        dist = defaultdict(tuple)
        prev = defaultdict(tuple)

        for y, row in enumerate(graph):
            for x, col in enumerate(row):
                q.add((y, x))
                dist[(y, x)] = float('inf')
                prev[(y, x)] = None
        dist[source] = 0

        with tqdm(total=len(q)) as pbar:
            while q:
                pbar.update(1)
                u = sorted({k: v for k,v in dist.items() if k in q}.items(), key=lambda x: x[1])[0][0]
                q.remove(u)
                if u == target:
                    break
                for (vy, vx) in get_neighbors(graph, u[0], u[1]):
                    if (vy, vx) not in q:
                        continue
                    alt = dist[u] + graph[vy][vx]
                    if alt < dist[(vy, vx)]:
                        dist[(vy, vx)] = alt
                        prev[(vy, vx)] = u

        s = []
        u = target
        if prev[u] is not None or u == source:
            while u is not None:
                s.insert(0, u)
                u = prev[u]

        return sum([graph[p[0]][p[1]] for p in s[1:]])

    return dijkstra(graph, (0, 0), (len(graph)-1, len(graph[0])-1))

def part2(graph):
    
    def increment_graph(n):
        g = graph.copy()
        for y, row in enumerate(g):
            for x, col in enumerate(row):
                g[y][x] = 1 + (g[y][x] + n - 1) % (9)
        return g

    full_graph = np.concatenate(tuple([increment_graph(n) for n in range(5)]), axis=1)
    for i in range(1, 5):
        full_graph = np.concatenate((full_graph, np.concatenate(tuple([increment_graph(n) for n in range(i, i+5)]), axis=1)))

    def dijkstra_pq(graph, source, target):

        pq = minpq()
        dist = defaultdict(tuple)
        prev = defaultdict(tuple)

        dist[source] = 0
        prev[source] = None

        for y, row in enumerate(graph):
            for x, col in enumerate(row):
                if (y, x) != source:
                    dist[(y, x)] = float('inf')
                    prev[(y, x)] = None
                pq[(y, x)] = dist[(y, x)]

        with tqdm(total=len(pq)) as pbar:
            while len(pq) > 0:
                pbar.update(1)
                u = pq.pop()
                for (vy, vx) in get_neighbors(graph, u[0], u[1]):
                    alt = dist[u] + graph[vy][vx]
                    if alt < dist[(vy, vx)]:
                        dist[(vy, vx)] = alt
                        prev[(vy, vx)] = u
                        pq[(vy, vx)] = alt

        s = []
        u = target
        if prev[u] is not None or u == source:
            while u is not None:
                s.insert(0, u)
                u = prev[u]

        return sum([graph[p[0]][p[1]] for p in s[1:]])
    
    return dijkstra_pq(full_graph, (0, 0), (len(full_graph)-1, len(full_graph[0])-1))
