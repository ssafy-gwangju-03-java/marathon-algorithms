# 1941 소문난 칠공주

# 가능한 모든 경우의수를 combinations로 뽑아서 bfs 돌리기

from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(lst):
    link = 0
    q = deque()
    q.append(lst[0])
    vis[lst[0][0]][lst[0][1]] = 0
    while q:
        y, x = q.popleft()
        link += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if [ny, nx] in lst and vis[ny][nx]:
                vis[ny][nx] = 0
                q.append((ny, nx))
    return link


lst = [list(map(str, input())) for _ in range(5)]
chk = []
for i in range(5):
    for j in range(5):
        chk.append([i, j])
cnt = 0
for i in combinations(chk, 7):
    vis = [[0] * 5 for _ in range(5)]
    anss = 0
    ansy = 0
    for k in i:
        vis[k[0]][k[1]] = 1
        if lst[k[0]][k[1]] == "S":
            anss += 1
        else:
            ansy += 1
    if ansy >= 4:
        continue
    ans = bfs(i)
    if ans == 7:
        cnt += 1
print(cnt)
