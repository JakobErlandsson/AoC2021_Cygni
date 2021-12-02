from os import getenv
input = [int(i) for i in open('input.txt', 'r').read()[:-1].split('\n')]
print(sum([input[i+1] > input[i] for i in range(len(input)-1)]) if getenv('part') == 'part1' else sum([input[i+3] > input[i] for i in range(len(input)-3)]))