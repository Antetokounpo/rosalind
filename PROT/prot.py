import sys

with open('rna_codon.txt', 'r') as f:
    table = f.read()

table = list(filter(bool, table.replace('\n', ' ').split(' ')))
table = dict([(table[i], table[i+1])for i in range(0, len(table), 2)])

with open(sys.argv[1], 'r') as f:
    s = f.read().strip()

ps = ''
for i in range(0, len(s), 3):
    amino = table[s[i:i+3]]
    if amino == 'Stop':
        break
    ps += amino
print(ps)