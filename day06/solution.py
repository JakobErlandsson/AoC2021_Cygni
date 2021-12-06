import sys, os
input = [int(i) for i in open('input.txt', 'r').read()[:-1].split(',')]
fish = [input.count(i) for i in range(10)]
for t in range(256):
    (new_8,new_6) = (fish[0],fish[0])
    fish = [fish[i+1] for i in range(8)] + [new_8]
    fish[6] += new_6
    if os.getenv('part') == 'part1' and t == 79:
        sys.exit("{}".format(sum([fish[i] for i in range(len(fish))])))
print(sum([fish[i] for i in range(len(fish))]))