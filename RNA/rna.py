import sys

f = open(sys.argv[1])
ds = f.read().strip()
f.close()

print(ds.replace('T', 'U'))