from functools import reduce

with open('rna_codon.txt', 'r') as f:
    table = f.read().strip()

table = list(filter(bool, table.replace('\n', ' ').split(' ')))
table = dict([(table[i], table[i+1])for i in range(0, len(table), 2)])

print(str(table.items()).replace('\'', '"'))