from os import getenv
input = [i for i in open('input.txt', 'r').read()[:-1].split('\n')]
(dots,folds) = ([i.split(',') for i in input[:-13]], input[-12:])
(xs, ys) = ([int(x) for (x,y) in dots], [int(y) for (x,y) in dots])
for (i,f) in enumerate(folds):
    f = f.split(' ')[-1].split('=')

    if f[0] == 'x': xs = [x if x < int(f[1]) else int(f[1]) - (x - int(f[1])) for x in xs]
    else:           ys = [y if y < int(f[1]) else int(f[1]) - (y - int(f[1])) for y in ys]

    if getenv('part') == 'part1' and i == 0: exit('{}'.format(len(set(zip(xs, ys)))))
for y in range(max(ys)+1): print(''.join(['X' if (x,y) in set(zip(xs,ys)) else ' ' for x in range(max(xs)+1)]))
