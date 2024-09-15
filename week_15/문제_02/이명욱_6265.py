import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

h, w = map(int, sys.stdin.readline().split())
image = [[0] * (w + 1)]
for i in range(h):
    tmp = list(map(int, sys.stdin.readline().split()))
    image.append([0] + tmp)

q = int(sys.stdin.readline())
for _ in range(q):
    x, y, c = map(int, sys.stdin.readline().split())
    now = image[x][y]
    if now == c:
        continue
    q = deque()
    image[x][y] = c
    q.append((x, y))
    while q:
        i, j = q.popleft()
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 1 <= nx <= h and 1 <= ny <= w:
                if image[nx][ny] == now:
                    image[nx][ny] = c
                    q.append((nx, ny))

for i in range(1, h + 1):
    print(' '.join(map(str, image[i][1:])))


# 참고: https://talktato.tistory.com/34