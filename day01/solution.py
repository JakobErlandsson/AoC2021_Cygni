from os import getenv
input = [int(i) for i in open('input.txt', 'r').read()[:-1].split('\n')]

def get_primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

if getenv('part') == 'part1':
    print(sum([i*n*(n in get_primes(max(input))) for (i,n) in enumerate(input)]))
else: # part == 'part2'
    print(sum([n*(n not in get_primes(max(input)))*(-1 if i%2 == 1 else 1) for (i,n) in enumerate(input)]))