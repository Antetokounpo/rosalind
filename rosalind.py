import sys

def fasta(filename):
    with open(filename, 'r') as f:
        txt = f.read()
        d = txt.split('>')
        k = [i.split('\n')[0] for i in d]
        v = [''.join(i.split('\n')[1:]) for i in d]
        return dict(zip(k[1:], v[1:]))