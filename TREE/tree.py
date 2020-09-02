import sys

with open(sys.argv[1], 'r') as f:
    ds = f.read()

n = int(ds.split('\n')[0])
e = [tuple(map(int, i.split(' '))) for i in ds.split('\n')[1:-1]]

def matrix_graph(n, e):
    m = [[0 for j in range(n)] for i in range(n)]
    for i, j in e:
        m[i-1][j-1] = 1
        m[j-1][i-1] = 1
    return m

def dfs(g, v, discovered=[]):
    discovered.append(v)
    for i in range(len(g[v])):
        if g[v][i] == 1 and not i in discovered:
            dfs(g, i, discovered)
    return discovered

def count_trees(g):
    l = set([i for i in range(len(g))])
    c = 0
    for _ in range(len(l)):
        l -= set(dfs(g, list(l)[0]))
        c += 1
        if not l:
            break
    return c-1

m = matrix_graph(n, e)
print(count_trees(m))
print(n-1-len(e))