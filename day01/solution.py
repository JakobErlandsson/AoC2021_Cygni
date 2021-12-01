from os import getenv
input = [int(i) for i in open('input.txt', 'r').read()[:-1].split('\n')]
print(sum([input[i+1] > input[i] for i in range(len(input)-1)]) if getenv('part') == 'part1' else sum([sum(input[i+1:i+4]) > sum(input[i:i+3]) for i in range(len(input)-3)]))

