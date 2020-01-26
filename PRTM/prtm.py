import sys

with open(sys.argv[1], 'r') as f:
    p = f.read().strip()

with open('mass_table.txt', 'r') as f:
    table = f.read().strip()

table = table.split('\n')
table = dict([tuple(filter(bool, i.split(' '))) for i in table])

print(sum([float(table[i]) for i in p]))
