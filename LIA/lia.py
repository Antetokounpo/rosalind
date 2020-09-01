import sys
import itertools
import operator
from functools import reduce
from math import factorial

with open(sys.argv[1], 'r') as f:
    ds = f.read()

k, n = map(int, ds.split())

print(k, n)

def comb(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def breed(p):
    sp = list(itertools.product(*p))
    om = list(itertools.product(*[('A', 'a'), ('B', 'b')]))

    return list(map(lambda x: (tuple(sorted((x[0][0], x[1][0]))), tuple(sorted((x[0][1], x[1][1])))), itertools.product(sp, om))) # transpose

def occurences(x):
    occs = {}
    for i in x:
        j = str(i)
        if j in occs.keys():
            occs[j] += 1
        else:
            occs[j] = 1
    return occs

def prob(n, r, k=1):
    t = 0
    for i in range(k, n):
        t += comb(n, i) * r**(n-i)
    return t+comb(n, n)

def binom_prob(n, k, p):
    return comb(n, k)*(p**k)*(1-p)**(n-k)

#g1 = breed((('A', 'a'), ('B', 'b')))
#g = g1
#for i in range(k-1):
#    g = list([breed(j) for j in g])
#    g = [item for sublist in g for item in sublist]

#c = g.count((('A', 'a'), ('B', 'b')))
#print(c)
#print(c/len(g))
#l = c/len(g)

k = 2**k
print(sum([binom_prob(k, i, 0.25) for i in range(n, k+1)])) # loi binomiale cumulative
print(prob(k, 3, k=n)/(4**k))
