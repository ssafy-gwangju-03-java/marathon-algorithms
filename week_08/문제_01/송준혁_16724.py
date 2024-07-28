# https://www.acmicpc.net/problem/16724

import sys

sys.setrecursionlimit(10**3)

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]

# 상 하 좌 우
d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
visited = [[0] * M for _ in range(N)]
safe_zones = 0


def dfs(r, c, path):
    # 이미 사이클이 발생한 장소라면
    if visited[r][c] == 2:
        # 현재 위치로 오는 모든 경로를 사이클 발생 경로로 설정
        for i, j in path:
            visited[i][j] = 2
        # 이미 사이클이 발생한 경로였기에 SAFE ZONE 개수는 변동 없음
        return 0

    # 현재 위치가 이전에 방문했던 곳이라면 사이클 발생
    if visited[r][c] == 1:
        # 현재 위치로 오는 모든 경로를 사이클 발생 경로로 설정
        for i, j in path:
            visited[i][j] = 2
        # 사이클 발생 == SAFE ZONE
        return 1

    visited[r][c] = 1

    command = grid[r][c]
    nr, nc = r + d[command][0], c + d[command][1]
    return dfs(nr, nc, path + [(r, c)])


for r in range(N):
    for c in range(M):
        if visited[r][c] == 0:
            safe_zones += dfs(r, c, [])

print(safe_zones)
