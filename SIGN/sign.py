import sys
import operator
from itertools import chain, permutations

with open(sys.argv[1], 'r') as f:
    ds = f.read()

n = int(ds)

nplus = range(1, n+1)
nminus = map(operator.neg, reversed(nplus))

perms = list(filter(lambda x: len(list(map(abs, x))) == len(list(set(map(abs, x)))), permutations(chain(nminus, nplus), n)))
print(len(perms))
for i in perms:
    print(*i)