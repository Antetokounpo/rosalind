import sys
from math import factorial, log10

with open(sys.argv[1], 'r') as f:
    dna, a = f.read().strip().split('\n')
a = list(map(float, a.split()))

print(*[log10((g/2)**(dna.count('G')+dna.count('C'))*((1.0-g)/2)**(dna.count('A')+dna.count('T'))) for g in a])
