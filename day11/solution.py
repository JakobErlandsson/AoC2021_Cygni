import os, sys, itertools
input = [int(j) for j in ''.join([i for i in open('input.txt', 'r').read()[:-1].split('\n')])]

def get_neighbours(idx, size):
    all_neighbours = [idx-size-1, idx-size, idx-size+1, idx-1, idx+1, idx+size-1, idx+size, idx+size+1]
    if idx % size == 0:      all_neighbours = [n for n in all_neighbours if n not in [idx-size-1, idx-1, idx+size-1]] # Left column
    if idx < size:           all_neighbours = [n for n in all_neighbours if n not in [idx-size-1, idx-size, idx-size+1]] # Top row
    if idx % size == size-1: all_neighbours = [n for n in all_neighbours if n not in [idx-size+1, idx+1, idx+size+1]] # Right column
    if idx >= size*(size-1): all_neighbours = [n for n in all_neighbours if n not in [idx+size-1, idx+size, idx+size+1]] # Bottom row
    return all_neighbours

(neighbours, tot_flashes) = ([get_neighbours(i, 10) for (i,_) in enumerate(input)], 0)
for t in itertools.count(start=1): 
    input = list(map(lambda x : x+1, input))
    flashes = set([i for (i,x) in enumerate(input) if x > 9])
    new_flashes = list(flashes)
    while new_flashes:
        for f in new_flashes:
            flashes.add(f)
            for n in neighbours[f]: input[n] += 1
        new_flashes = [i for (i,x) in enumerate(input) if x > 9 and i not in flashes]
    input = [i if i <= 9 else 0 for i in input]
    tot_flashes += len(flashes)
    if os.getenv('part') == 'part1' and t == 100: sys.exit('{}'.format(tot_flashes))
    if os.getenv('part') == 'part2' and len(flashes) == 100: sys.exit('{}'.format(t))