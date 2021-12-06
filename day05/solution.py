from os import getenv
input = [i.split(' -> ') for i in open('input.txt', 'r').read()[:-1].split('\n')]
grid = [[0]*1000 for i in range(1000)]
for i in input:
    ([x1, y1], [x2, y2]) = (map(int, i[0].split(',')), map(int, i[1].split(',')))
    (x_start, y_start) = (x1 if x1 < x2 else x2, y1 if y1 < y2 else y2)
    (x_range, y_range) = (range(y_start, y_start + abs(y1-y2)+1), range(x_start, x_start + abs(x1-x2)+1))
    if x1 == x2:
        for j in x_range:
            grid[j][x1] += 1
    elif y1 == y2:
        for j in y_range:
            grid[y1][j] += 1
    elif getenv('part') == 'part2' and abs(x1-x2) == abs(y1-y2): 
        if (x1 > x2 and y1 > y2) or (x2 > x1 and y2 > y1):
            diag_range = zip(x_range, y_range)
        elif x1 < y1:
            diag_range = zip(reversed(x_range), y_range)
        else:
            diag_range = zip(x_range, reversed(y_range))
        for (j,k) in diag_range:
                grid[j][k] += 1
    
print(sum([grid[i][j] > 1 for i in range(1000) for j in range(1000)]))