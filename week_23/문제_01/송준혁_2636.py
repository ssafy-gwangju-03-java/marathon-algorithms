# https://www.acmicpc.net/problem/2636

import sys
from collections import deque

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C


def melter():
    q = deque()
    q.append((0, 0))
    visited = [[0] * C for _ in range(R)]
    visited[0][0] = 1
    to_melt = []

    while q:
        r, c = q.popleft()

        # 그리드를 순회하면서 상하좌우 탐색 후 치즈가 아닌 부분은 덱에 삽입해 방문 예약
        # 탐색 후 방문 처리가 안됐고 치즈인 부분은 녹일 배열에 삽입
        for i in range(4):
            nr, nc = r + d[i][0], c + d[i][1]

            if is_valid(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = 1
                if grid[nr][nc] == 0:
                    q.append((nr, nc))
                else:
                    to_melt.append((nr, nc))

    # 치즈 녹이기
    for r, c in to_melt:
        grid[r][c] = 0

    return len(to_melt)


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
time, count = 0, 0

while True:
    melted = melter()
    if melted == 0:
        break
    else:
        time += 1
        count = melted

print(time)
print(count)
