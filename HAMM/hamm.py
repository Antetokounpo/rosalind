import sys

f = open(sys.argv[1], 'r')
ds = f.read().strip()
f.close()

s = ds.split('\n')[0]
t = ds.split('\n')[1]

hamming = 0
for i, j in zip(s, t):
    if i != j:
        hamming += 1
print(hamming)