import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def count_ocean(r, c):
    count = 0

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            count += 1

    return count


# 빙산 개수 세기
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))


iceberg = 1
year = 0
while iceberg == 1:
    iceberg = 0
    year += 1

    # 녹을 높이 저장
    melt = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                melt.append((i, j, count_ocean(i, j)))

    # 녹이기
    for r, c, count in melt:
        arr[r][c] = 0 if arr[r][c] - count < 0 else arr[r][c] - count

    # 빙산 개수 세기
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j)
                iceberg += 1

    # 빙산이 쪼개지지 않으면
    if iceberg == 0:
        year = 0
        break

print(year)
