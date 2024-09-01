import sys

"""
반례

4 6
1 2
2 1
2 3
3 2
1 3
2 4
1 3
"""

def dfs(curr, adj, visited):
    if visited[curr]:
        return
    else:
        visited[curr] = True
        for next in adj[curr]:
            dfs(next, adj, visited)
    return


N, m = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]
reverse_adjl = [[] for _ in range(N + 1)]

for _ in range(m):
    p, q, = map(int, sys.stdin.readline().split())
    adjl[p].append(q)
    reverse_adjl[q].append(p)

S, T = map(int, sys.stdin.readline().split())


fromS = [False] * (N + 1)
fromS[T] = 1
dfs(S, adjl, fromS)

fromT = [False] * (N + 1)
fromT[S] = 1
dfs(T, adjl, fromT)

toS = [False] * (N + 1)
dfs(S, reverse_adjl, toS)

toT = [False] * (N + 1)
dfs(T, reverse_adjl, toT)


count = 0

for i in range(1, N + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1

print(count - 2)