from os import getenv
input = [int(i) for i in open('input.txt', 'r').read()[:-1].split(',')]
print(min([sum([abs(i-p) for p in input]) for i in range(max(input))]) if getenv('part') == 'part1' else min([sum([((abs(i-p)+1)**2 - (abs(i-p)+1))//2 for p in input]) for i in range(max(input))]))