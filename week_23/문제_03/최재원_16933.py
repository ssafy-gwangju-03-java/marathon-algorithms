from collections import deque
import sys

sys.stdin = open('../../input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs():
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0, True, 1))

    while q:
        r, c, z, daytime, ans = q.popleft()

        if r == N - 1 and c == M - 1:
            print(ans)
            exit()

        for k in range(4):
            nx = r + dr[k]
            ny = c + dc[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = ans
                    q.append((nx, ny, z, not daytime, ans + 1))
                if board[nx][ny] == 1 and z < K and visited[nx][ny][z + 1] == 0:
                    if daytime:
                        visited[nx][ny][z + 1] = ans
                        q.append((nx, ny, z + 1, not daytime, ans + 1))
                    else:
                        q.append((r, c, z, not daytime, ans + 1))

    print(-1)


bfs()
