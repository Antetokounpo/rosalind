import sys

with open(sys.argv[1], 'r') as f:
    ds = f.read()

def fasta(txt):
    f = txt.split('>')
    k = [i.split('\n')[0] for i in f]
    v = [''.join(i.split('\n')[1:]) for i in f]
    return dict(zip(k[1:], v[1:]))

graph = []

for k, v in fasta(ds).items():
    for i, j in fasta(ds).items():
        if k != i:
            if v[-3:] == j[:3]:
                graph.append((k, i))

for i, j in graph:
    print(i + ' ' + j)