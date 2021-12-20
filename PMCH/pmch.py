import sys
from math import factorial

with open(sys.argv[1], 'r') as f:
    ds = f.read().strip()

def fasta(txt):
    f = txt.split('>')
    k = [i.split('\n')[0] for i in f]
    v = [''.join(i.split('\n')[1:]) for i in f]
    return dict(zip(k[1:], v[1:]))

rna = list(fasta(ds).values())[0]

v = list(rna)
edges1 = []
edges2 = []

for i, v1 in enumerate(v):
    for j, v2 in enumerate(v):
        pair = v1+v2
        if pair == 'AU' and (i not in edges1 and j not in edges1):
            edges1.append(i)
            edges1.append(j)
        if pair == 'CG' and (i not in edges2 and j not in edges2):
            edges2.append(i)
            edges2.append(j)

print(factorial(len(edges1)//2)*factorial(len(edges2)//2))