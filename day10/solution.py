from os import getenv
input = [i for i in open('input.txt', 'r').read()[:-1].split('\n')]
(opening, closing, opposite, score, score2) = ({'(': 0, '[': 0, '{': 0, '<': 0}, {')': 0, ']': 0, '}': 0, '>': 0}, {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<'}, {')': 3, ']': 57, '}': 1197, '>': 25137}, {')': 1, ']': 2, '}': 3, '>': 4})
(fault, fault2_list) = (0, [])
for line in input:
    (open_stack, fault2, wrong) = ([], 0, False)
    for c in line:
        if c in closing:
            if open_stack[-1] != opposite[c]:
                (fault, wrong) = (fault + score[c], True)
            else: open_stack.pop()
        else: open_stack.append(c)        
    if getenv('part') == 'part2' and not wrong:
        completion = [opposite[c] for c in reversed(open_stack)]
        for c in completion:
            fault2 = (fault2 * 5) + score2[c]
        fault2_list.append(fault2)
if getenv('part') == 'part1': print(fault)
if getenv('part') == 'part2': print(sorted(fault2_list)[len(fault2_list)//2])