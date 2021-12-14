from os import getenv
input = [i.split(' | ') for i in open('input.txt', 'r').read()[:-1].split('\n')]
if getenv('part') == 'part1': print(sum([sum([len(sig) in [2,3,4,7] for sig in sig_out.split(' ')]) for (_,sig_out) in input]))
else:
    (numbers, ans) = ({'012456':'0','25':'1','02346':'2','02356':'3','1235':'4','01356':'5','013456':'6','025':'7','0123456':'8','012356':'9'}, 0)
    for (s_in, s_out) in input:
        s = sorted(s_in.split(' '), key=len)
        (size_5, size_6, mapping) = (s[3]+s[4]+s[5], s[6]+s[7]+s[8], ['']*7)
        mapping[0] = [c for c in s[1] if c not in s[0]][0] 
        mapping[2] = [c for c in s[0] if size_6.count(c) == 2][0]
        mapping[5] = [c for c in s[0] if c != mapping[2]][0]
        mapping[4] = [c for c in s[9] if (s[2]+size_6).count(c) == 2][0]
        mapping[3] = [c for c in s[9] if (size_6+mapping[2]+mapping[4]).count(c) == 2][0]
        mapping[1] = [c for c in s[9] if (size_5+mapping[4]).count(c) == 1][0]
        mapping[6] = [c for c in s[9] if c not in ''.join(mapping)][0]
        ans += int(''.join([numbers[''.join(sorted([str(mapping.index(c)) for c in o]))] for o in s_out.split(' ')]))
    print(ans)