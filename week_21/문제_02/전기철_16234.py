#16234 인구 이동
from collections import deque

n, l, r = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    ans = []
    queue.append((i, j))
    ans.append((i, j))
    while queue:
        y,x = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not vis[ny][nx]:
                if l <= abs(lst[ny][nx] - lst[y][x]) <= r:
                    vis[ny][nx] = 1
                    queue.append((ny, nx))
                    ans.append((ny, nx))
    return ans               
result = 0
while True:
    vis = [[0 for _ in range(n)] for _ in range(n)]
    chk = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                vis[i][j] = 1
                country = bfs(i, j)
                
                if len(country) > 1:
                    chk = 1
                    man = sum(lst[y][x] for y, x in country) // len(country)
                    for y, x in country:
                        lst[y][x] = man
    if chk == 0:
        print(result)
        break

    result += 1