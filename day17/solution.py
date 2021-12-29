import math, itertools, os
input = open('input.txt', 'r').read()[:-1].split(' ')[2:]

(min_x, max_x) = map(int, input[0].replace('x=', '').replace(',', '').split('..'))
(min_y, max_y) = map(int, input[1].replace('y=', '').split('..'))

y_diff = max_y-min_y

def fire(velocity):
    (x, y) = (0,0)
    (x_vel, y_vel) = velocity
    highest_y = -math.inf
    while True:
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return highest_y
        if x > max_x or y < min_y:
            return -math.inf
        x += x_vel
        y += y_vel
        if x_vel != 0:
            x_vel += (1 if x_vel < 0 else -1)
        y_vel -= 1
        highest_y = max(highest_y, y)

heights = []
for x in range(max_x+1):
    for y in itertools.count(start=min_y):
        height = fire((x,y))
        heights.append(height)
        if y > y_diff and all([h == -math.inf for h in heights[-y_diff*2:]]): #somewhat arbitrary point where i stop looking
            break

if os.getenv('part') == 'part1': print(max(heights))
if os.getenv('part') == 'part2': print(sum([h != -math.inf for h in heights]))