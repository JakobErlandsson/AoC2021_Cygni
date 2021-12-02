from os import getenv
input = [i.split(' ') for i in open('input.txt', 'r').read()[:-1].split('\n')]
if getenv('part') == 'part1': 
    print(sum([int(i[1]) for i in input if i[0] == 'forward']) * sum([int(i[1]) if i[0] == 'down' else -int(i[1]) if i[0] == 'up' else 0 for i in input]))
elif getenv('part') == 'part2':
    (aim, depth) = (0,0)
    for i in input:
        aim += int(i[1]) if i[0] == 'down' else -int(i[1]) if i[0] == 'up' else 0 
        depth += aim*int(i[1]) if i[0] == 'forward' else 0
    print(depth*sum([int(i[1]) for i in input if i[0] == 'forward']))