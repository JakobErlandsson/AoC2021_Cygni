import math, os, queue
input = ''.join([i for i in open('input.txt', 'r').read()[:-1].split('\n')])
row_length = 100
input = {(i % row_length, i // row_length) : int(v) for (i,v) in enumerate(input)}

if os.getenv('part') == 'part2':
    p2_input = input.copy()
    for (x,y) in input:
        for (dx,dy) in [(x2,y2) for x2 in range(5) for y2 in range(5)][1:]:
            new_point = (x+dx*row_length, y+dy*row_length)
            new_val = input[(x,y)] + (dx+dy)
            p2_input[new_point] = new_val % 9 if new_val != 9 else 9
    input = p2_input
    row_length *= 5

def get_neighbours(i, size):
    (x,y) = i
    all_neighbours = [(x,y-1), (x-1,y), (x+1,y), (x,y+1)]
    if y == 0:      all_neighbours.remove((x,y-1))
    if x == 0:      all_neighbours.remove((x-1,y))
    if y == size-1: all_neighbours.remove((x,y+1))
    if x == size-1: all_neighbours.remove((x+1,y))
    return all_neighbours

neighbours = {i:get_neighbours(i, row_length) for i in input}

def djikstra(graph, start):
    D = {v:math.inf for v in graph}
    D[start] = 0

    pq = queue.PriorityQueue()
    pq.put((0, start))

    visited = set()
    while not pq.empty():
        (_, current) = pq.get()
        visited.add(current)

        for n in neighbours[current]:
            dist = input[n]
            if n not in visited:
                new_cost = D[current] + dist
                if new_cost < D[n]:
                    pq.put((new_cost, n))
                    D[n] = new_cost
    return D

path = djikstra(input, (0,0))
print(path[(row_length-1, row_length-1)])
