import sys

f = open(sys.argv[1])
ds = f.read().strip()
f.close()

factors = (1., 1., 1., 0.75, 0.5, 0.)
nb_couples = [int(i) for i in ds.split(' ')]

expected = 0
for (c, f) in zip(nb_couples, factors):
    expected += 2*f*c
print(expected)
