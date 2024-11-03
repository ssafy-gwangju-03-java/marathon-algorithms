import sys
from collections import deque

input = sys.stdin.read

data = input().splitlines()
N, M = map(int, data[0].split())
a = [list(map(int, row.split())) for row in data[1:]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
score = 0

while True:
    visited = [[0] * N for _ in range(N)]
    blocks = [] 

    for i in range(N):
        for j in range(N):
            if a[i][j] > 0 and not visited[i][j]: 
                color = a[i][j]
                q = deque([[i, j]])
                visited[i][j] = 1
                block_cnt, rainbow_cnt = 1, 0
                blocks_group, rainbow_blocks = [[i, j]], []

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if a[nx][ny] == color or a[nx][ny] == 0:
                                visited[nx][ny] = 1
                                q.append([nx, ny])
                                block_cnt += 1
                                blocks_group.append([nx, ny])
                                if a[nx][ny] == 0:
                                    rainbow_cnt += 1
                                    rainbow_blocks.append([nx, ny])

                for rx, ry in rainbow_blocks:
                    visited[rx][ry] = 0

                if block_cnt >= 2:
                    blocks.append([block_cnt, rainbow_cnt, blocks_group])

    blocks.sort(reverse=True)

    if not blocks:
        break

    for x, y in blocks[0][2]:
        a[x][y] = -2
    score += blocks[0][0] ** 2

    # 중력 적용
    for j in range(N):
        for i in range(N - 2, -1, -1):
            if a[i][j] > -1:
                r = i
                while r + 1 < N and a[r + 1][j] == -2:
                    a[r + 1][j] = a[r][j]
                    a[r][j] = -2
                    r += 1

    # 90도 반시계 회전
    new_a = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_a[N - 1 - j][i] = a[i][j]
    a = new_a

    # 중력 재적용
    for j in range(N):
        for i in range(N - 2, -1, -1):
            if a[i][j] > -1:
                r = i
                while r + 1 < N and a[r + 1][j] == -2:
                    a[r + 1][j] = a[r][j]
                    a[r][j] = -2
                    r += 1

print(score)
