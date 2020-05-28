import sys

with open(sys.argv[1], 'r') as f:
    n, k = f.read().strip().split()

n = int(n)
k = int(k)

p = 1
for i in range(n, n-k, -1):
    p *= i
print(p % 1000000)