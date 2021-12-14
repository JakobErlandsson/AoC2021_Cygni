from os import getenv
input = [i.split(' -> ') for i in open('input.txt', 'r').read()[:-1].split('\n') if i]
(substitutions, polymer) = ({s[0]:s[1] for s in input[1:]}, input[0][0])
elements = {i:polymer.count(i) for i in set(polymer)}
polymer = [polymer[i] + polymer[i+1] for i in range(len(polymer)-1)]
polymer_count = {p:polymer.count(p) for p in polymer}

for t in range(40):
    new_pol_count = {}
    for k, v in polymer_count.items():
        to_add = (k[0] + substitutions[k], substitutions[k] + k[1])
        if substitutions[k] in elements: elements[substitutions[k]] += v
        else:                            elements[substitutions[k]] = v
        for l in to_add:
            if l in new_pol_count: new_pol_count[l] += v
            else:                new_pol_count[l] = v
    polymer_count = new_pol_count
    if getenv('part') == 'part1' and t == 9: print(max(elements.values()) - min(elements.values()))

if getenv('part') == 'part2': print(max(elements.values()) - min(elements.values()))