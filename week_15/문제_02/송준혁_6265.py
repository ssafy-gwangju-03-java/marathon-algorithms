# https://softeer.ai/practice/6265

## Referenced
# https://jie0025.tistory.com/450

import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid(r, c):
    return 0 <= r < H and 0 <= c < W


def processor(i, j, color, current):
    queue = deque()
    queue.append((i, j))
    # 현재 위치 색 변경
    image[i][j] = color
    visited = [[0] * W for _ in range(H)]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r + d[i][0], c + d[i][1]

            # 방문한 적 없고 현재 색과 동일한 픽셀이면
            if is_valid(nr, nc) and not visited[nr][nc] and image[nr][nc] == current:
                # 방문처리, 색 변경 후 다음 방문 예약
                visited[nr][nc] = 1
                image[nr][nc] = color
                queue.append((nr, nc))


H, W = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())

for _ in range(Q):
    i, j, c = map(int, input().split())
    i -= 1
    j -= 1
    processor(i, j, c, image[i][j])

for r in range(H):
    for c in range(W):
        print(image[r][c], end=" ")
    print()
