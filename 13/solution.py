## advent of code 2020
## https://adventofcode.com/2020
## day 13

from sympy.ntheory.modular import crt

with open('input.txt', 'r') as f:
    delay = int(f.readline())
    buses = f.readline().split(',')

# part one ------------------------------------------------

bus_ids = [int(x) for x in buses if x != 'x']

min_depart = float('inf')
depart_bus = None
for bus in bus_ids:
    i = delay
    while True:
        if i % bus == 0:
            if i < min_depart:
                min_depart = i
                depart_bus = bus
            break
        else:
            i += 1

print((min_depart - delay) * depart_bus)

# part two ------------------------------------------------

N, A = [], []
for i, id in enumerate(buses):
    if id != 'x':
        N.append(int(id)); A.append(int(id) - i)

print(crt(N, A)[0])
