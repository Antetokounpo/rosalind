import sys

with open(sys.argv[1], 'r') as f:
    ds = f.read()

ds = ds.split("\n")
n = int(ds[0])
p = list(map(int, ds[1].split()))

def find_longuest_seq(l):
    n = len(l)
    lis = [1]*n
    lisn = [[i] for i in l]

    for i in range(1, n):
        for j in range(0, i):
            if l[i] > l[j] and lis[i] < lis[j] + 1:
                lisn[i] = [lisn[i][0]] + lisn[j]
                lis[i] = lis[j] + 1
    return reversed(max(lisn, key=len))

print(*find_longuest_seq(p))
print(*map(abs, find_longuest_seq([-x for x in p])))
