from os import getenv
input = [i for i in open('input.txt', 'r').read()[:-1].split('\n') if i]
boards = [[x.split(' ') for x in input[i:i+5]] for i in range(1, len(input)-4, 5)]
winning_combinations = [list(range(i, i+5)) for i in range(0, 25, 5)] + [[i+5*j for j in range(5)] for i in range(5)]
(hits, scores) = ({i:[] for i in range(len(boards))}, [])
for number in input[0].split(','):
    for (i, board) in enumerate(boards):
        if hits[i] != 'won': 
            board_list = [a for b in board for a in b if a]
            if number in board_list: 
                hits[i].append(board_list.index(number))
                if len(hits[i]) >= 5 and any(all([n in hits[i] for n in c]) for c in winning_combinations):
                    scores.append(sum([int(n) for (k,n) in enumerate(board_list) if k not in hits[i]]) * int(number))
                    hits[i] = 'won'
print(scores[0] if getenv('part') == 'part1' else scores[-1])