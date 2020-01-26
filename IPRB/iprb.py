import sys

f = open(sys.argv[1])
ds = f.read().strip()
f.close()

k, m, n = ds.split(' ')
k, m, n = int(k), int(m), int(n)
pop = k + m + n

probs = [
    (k/pop) * ((k-1)/(pop-1)),
    (k/pop) * (m/(pop-1)),
    (k/pop) * (n/(pop-1)),

    (m/pop) * (k/(pop-1)),
    (m/pop) * ((m-1)/(pop-1)) * 0.75,
    (m/pop) * (n/(pop-1)) * 0.5,

    (n/pop) * (k/(pop-1)),
    (n/pop) * (m/(pop-1)) * 0.5,
]
print(probs)

prob = sum(probs)
print(prob)