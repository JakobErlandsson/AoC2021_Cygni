from os import getenv
input = ''.join([i for i in open('input.txt', 'r').read()[:-1].split('\n')])

def get_neighbours(i, row_length, n_rows):
    all_neighbours = [(i-row_length),(i-1), (i+1), (i+row_length)]
    if i % row_length == 0:               all_neighbours.remove((i-1)) ## along the left border
    if i % row_length == row_length-1:    all_neighbours.remove(i+1) ## along the right border
    if i < row_length:                    all_neighbours.remove(i-row_length) ## along the top border         
    if i >= row_length*n_rows-row_length: all_neighbours.remove(i+row_length)## along the bottom border
    return all_neighbours

def get_basin(point, accumulator):
    accumulator.add(point)
    non_9_neighbours = [n for n in neighbours[point] if input[n] != '9' and n not in accumulator]
    if non_9_neighbours != []:
        for n in non_9_neighbours:
            get_basin(n, accumulator)
    return accumulator

neighbours = [get_neighbours(i, 100, 100) for i in range(len(input))]
low_points = [i for (i, depth) in enumerate(input) if all([depth < input[j] for j in neighbours[i]])]
if getenv('part') == 'part1': print(sum([int(input[i])+1 for i in low_points]))
else:
    basins = sorted([len(get_basin(p, set())) for p in low_points])
    print(basins[-1]*basins[-2]*basins[-3])