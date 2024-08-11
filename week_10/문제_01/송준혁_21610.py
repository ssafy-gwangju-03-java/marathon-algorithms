# https://www.acmicpc.net/problem/21610

## Referenced
# https://jaehwaseo.tistory.com/26

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

# 좌 좌상 상 우상 우 우하 하 좌하
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 구름 생성 좌표
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for move in moves:
    d, s = move[0] - 1, move[1] % N
    has_rained = set()

    # 비 내리기
    while clouds:
        r, c = clouds.pop()
        nr, nc = (r + s * dr[d]) % N, (c + s * dc[d]) % N
        grid[nr][nc] += 1
        # 구름이 있던 자리는 저장해뒀다가 나중에 제외 시켜줌
        has_rained.add((nr, nc))

    # 물복사버그
    for r, c in has_rained:
        count = 0
        # 물이 증가한 칸의 대각선 방향 검사
        for i in range(1, 8, 2):
            nr, nc = r + dr[i], c + dc[i]
            # 격자를 벗어나지 않는 경우에만 물복사 버그 실행
            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc]:
                    count += 1
        grid[r][c] += count

    for r in range(N):
        for c in range(N):
            # 기존 구름 있던 자리가 아니고
            if (r, c) not in has_rained and grid[r][c] >= 2:
                # 물의 양이 2 이상인 곳 구름 생성 후 물 양 줄이기
                clouds.append((r, c))
                grid[r][c] -= 2

print(sum([sum(_) for _ in grid]))
