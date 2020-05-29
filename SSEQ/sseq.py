import sys; sys.path.append('..')
from rosalind import *
from functools import reduce

s, t = fasta(sys.argv[1]).values()

print(*reduce((lambda l, c: l + [s.find(c, l[-1] if l else 0)+1]), t, []))