import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

V = int(input())
adjl = [[] for _ in range(V + 1)]

for _ in range(V):
    line = list(map(int, input().split()))
    node = line[0]
    for i in range(1, len(line) // 2):
        adjl[node].append((line[i * 2 - 1], line[i * 2]))


def bfs(x):
    visited = [-1] * (V + 1)
    q = deque()
    q.append(x)
    visited[x] = 0
    dist = [0, 0]

    while q:
        node = q.popleft()
        for v, d in adjl[node]:
            if visited[v] == -1:
                visited[v] = visited[node] + d
                q.append(v)

                if visited[v] > dist[1]:
                    dist = [v, visited[v]]

    return dist


node = bfs(1)[0]
print(bfs(node)[1])

