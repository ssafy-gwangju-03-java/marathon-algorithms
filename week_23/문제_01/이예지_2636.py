# 2636 치즈
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append((0, 0))
    visited = [[False] * c for _ in range(r)] # visited 초기화
    visited[0][0] = True

    melted = []

    while Q:
        x, y = Q.popleft()

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < r and 0 <= ny < c):
                continue

            if not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    Q.append((nx, ny))
                else:
                    melted.append((nx, ny))
                visited[nx][ny] = True

    # 치즈 녹이기
    for x, y in melted:
        cheese[x][y] = 0

    return len(melted)



r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

time = 0
cnt = 0

while True:
    temp = bfs()
    if temp == 0:
        break
    time += 1
    cnt = temp

print(time)
print(cnt)