from os import getenv
input = [i for i in open('input.txt', 'r').read()[:-1].split('\n')]
gamma = ''.join(['1' if sum([int(j[i]) for j in input]) > len(input)/2 else '0' for i in range(len(input[0]))])
def find(list, high, index=0):
    if len(list) == 1:
        return (list[0])
    (l1, l2) = ([j for j in list if j[index] == '1'],[j for j in list if j[index] == '0'])
    return find(l1 if len(l1) >= len(l2) else l2, high, index+1) if high else find(l1 if len(l1) < len(l2) else l2, high, index+1)    
print(int(gamma, 2) * int(''.join(['1' if i == '0' else '0' for i in gamma]), 2) if getenv('part') == 'part1' else int(find(input, True), 2) * int(find(input, False), 2))