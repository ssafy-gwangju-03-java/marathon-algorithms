import sys
from collections import deque

N, K, R = map(int, sys.stdin.readline().split())

road = [[[] for _ in range(N)] for _ in range(N)]
for i in range(R):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

cows = []
for i in range(K):
    r, c = map(int, sys.stdin.readline().split())
    cows.append((r - 1, c - 1))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (nr, nc) not in road[r][c]:
                visited[nr][nc] = True
                q.append((nr, nc))

    return visited


answer = 0
for i in range(K):
    visited = bfs(cows[i][0], cows[i][1])

    for j in range(K):
        if not visited[cows[j][0]][cows[j][1]]:
            answer += 1

print(answer // 2)
