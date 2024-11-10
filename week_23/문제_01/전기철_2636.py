# 2636 치즈
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    chk = 0
    vis = [[0] * m for _ in range(n)]
    q = deque()
    q.append([0, 0])
    ans = []
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not vis[ny][nx]:
                vis[ny][nx] = 1
                if not lst[ny][nx]:
                    q.append((ny, nx))
                else:
                    ans.append((ny, nx))
                    chk += 1
    for t in ans:
        lst[t[0]][t[1]] = 0
    return chk


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
result, time = 0, 0
for i in lst:
    result += i.count(1)

while True:
    time += 1
    cnt = bfs()
    result -= cnt
    if not result:
        print(time), print(cnt)
        break
