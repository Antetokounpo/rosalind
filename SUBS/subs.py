import sys

f = open(sys.argv[1], 'r')
ds = f.read().strip()
f.close()

ds = ds.split('\n')
s = ds[0]
t = ds[1]

loc = []
for i in range(len(s) - len(t)+1):
    if s[i:len(t)+i] == t:
        loc.append(str(i+1))

out = ' '.join(loc)
print(out)