import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 테두리에 0 추가
board = [[0] * (M + 2) for _ in range(N + 2)]
for i in range(N):
    for j in range(M):
        board[i + 1][j + 1] = arr[i][j]
N = N + 2
M = M + 2


def bfs():
    q = deque()
    q.append((0, 0))

    visited = [[0] * (M + 2) for _ in range(N + 2)]
    visited[0][0] = 1

    border = []

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if board[nr][nc] == 0:
                    q.append((nr, nc))
                elif board[nr][nc] == 1:
                    border.append((nr, nc))

                visited[nr][nc] = 1

    return border


time = 0
cheese_count = sum(sum(r) for r in board)

while True:
    # 치즈 녹이기
    time += 1
    border = bfs()

    # 치즈 개수가 0개가 되면 빼지 않고 종료
    if len(border) - cheese_count == 0:
        break
    else:
        cheese_count -= len(border)

    # 테두리 0으로 만들기
    for r, c in border:
        board[r][c] = 0

print(time)
print(cheese_count)
