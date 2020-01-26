import sys

f = open(sys.argv[1])
ds = f.read().strip()
f.close()

s = ds[::-1]

pairs = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

out = ''.join([pairs[c] for c in s])
print(out)
