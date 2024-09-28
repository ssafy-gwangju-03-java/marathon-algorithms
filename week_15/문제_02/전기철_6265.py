# 6265 이미지 프로세싱
# 단순 bfs 문제
from collections import deque
import sys
input=sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x, now, change):
    global lst
    lst[y][x] = change
    vis= [[0]*w for _ in range(h)]
    vis[y][x]=1
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        lst[y][x] = change
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if lst[ny][nx] == now and not vis[ny][nx]:
                    lst[ny][nx] = change
                    vis[ny][nx]=1
                    q.append((ny, nx))


h, w = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
for _ in range(q):
    i, j, c = map(int, input().split())
    bfs(i - 1, j - 1, lst[i - 1][j - 1], c)
for i in lst:
    print(*i, end=" ")
    print()