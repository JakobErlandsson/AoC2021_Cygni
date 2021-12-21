from os import getenv
input = [i.split('-') for i in open('input.txt', 'r').read()[:-1].split('\n')]
(part, cave_map) = (getenv('part'), {})

for (start, end) in input:
    if start in cave_map: cave_map[start].append(end)
    else:                 cave_map[start] = [end]
    if end in cave_map:   cave_map[end].append(start)
    else:                 cave_map[end] = [start]
    
small = [c for c in cave_map if c not in ('end', 'start') and c.islower()]

def allowed(path, n):
    if part == 'part1':           return n not in path or n.isupper()
    else:
        if n in ('end', 'start'): return n not in path
        if n.isupper():           return True
        (cave_count, n_count) = ([path.count(i) for i in small], path.count(n))
        return all([x < 2 for x in cave_count]) or n_count == 0 

def get_all_paths(graph, node, path): # Djikstra
    path = path + [node]
    if node == 'end': return [path]
    paths = []
    for n in graph[node]:
        if allowed(path, n):
            new_paths = get_all_paths(graph, n, path)
            for p in new_paths:
                paths.append(p)
    return paths
    
print(len(get_all_paths(cave_map, 'start', []) ))
