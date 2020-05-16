import sys
from functools import reduce
import operator

with open(sys.argv[1], 'r') as f:
    ds = f.read().strip()
protein = ds

with open('rna_codon.txt', 'r') as f:
    table = f.read().strip()

table = list(filter(bool, table.replace('\n', ' ').split(' ')))
table = dict([(table[i], table[i+1])for i in range(0, len(table), 2)])
print(table.items())

table = dict([(v, len([i for i in table.keys() if v == table[i]])) for v in table.values()])
print(reduce(operator.mul, [table[i] for i in protein], 1)*table['Stop'] % 1000000)