import sys

f = open(sys.argv[1], 'r')
ds = f.read()
f.close()

nucleobases = {key: 0 for key in ['A', 'C', 'G', 'T']}

for c in ds:
    nucleobases[c] += 1

out = ' '.join([str(v) for v in nucleobases.values()])
print(out)