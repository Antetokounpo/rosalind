import sys

f = open(sys.argv[1], 'r')
ds = f.read().strip()
f.close()

ds = ds.split('>')[1:]
ds = dict([(i[:13], i[13:].replace('\n', '')) for i in ds])

gc_contents = dict()
for key, value in ds.items():
    gc_contents[key] = (value.count('G') + value.count('C')) / len(value) * 100.0
key = max(gc_contents, key=gc_contents.get)

print(key)
print(gc_contents[key])