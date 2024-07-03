import sys
from collections import deque

"""
특정한 이동 방식에 횟수가 정해져 있을 때 (제한되어 있을 때) 3차원 배열을 활용
== 벽 부수고 이동하기
"""

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

# 인접 4방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 말이 되어 움직이는 8방향
hr = [-1, -2, -2, -1, 1, 2, 2, 1]
hc = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs():
    global did_reach

    q = deque()

    # int[][][] visited = new int[K + 1][H][W];
    # K + 1개(점프가 가능한 횟수, 0 포함)의 visited 배열
    visited = [[[0] * W for _ in range(H)] for _ in range(K + 1)]

    q.append((0, 0, K))
    turn = 0

    while q:
        size = len(q)

        for _ in range(size):
            r, c, k = q.popleft()

            if r == H - 1 and c == W - 1:
                did_reach = True
                print(turn)
                return

            # 점프 횟수가 남아있을 때, 점프하는 경우의 수 추가
            if k:
                for d in range(8):
                    nr, nc = r + hr[d], c + hc[d]
                    if 0 <= nr < H and 0 <= nc < W and not visited[k-1][nr][nc] and not board[nr][nc]:
                        visited[k-1][nr][nc] = turn
                        q.append((nr, nc, k - 1))

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < H and 0 <= nc < W and not visited[k][nr][nc] and not board[nr][nc]:
                    visited[k][nr][nc] = turn
                    q.append((nr, nc, k))

        turn += 1


did_reach = False
bfs()
if not did_reach:
    print(-1)
