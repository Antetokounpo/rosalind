import sys

f = open(sys.argv[1], 'r')
df = f.read().strip().split(' ')
f.close()

n = int(df[0])
k = int(df[1])

a = 1
b = 1

for i in range(n-2):
    c = a
    a = b
    b = k*c + a
print(b)