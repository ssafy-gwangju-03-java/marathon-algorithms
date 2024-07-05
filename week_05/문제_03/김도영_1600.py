# 말이 되고픈 원숭이

from collections import deque

# 체스의 나이트와 같은 이동 방식(K번 까지만 움직일 수 있음)
di_n = [-2, -2, -1, -1, 1, 1, 2, 2]
dj_n = [-1, 1, -2, 2, -2, 2, -1, 1]

# 그 이외에는 상하좌우로밖에 못움직임
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

K = int(input())
W, H = map(int, input().split())

# 0은 평지, 1은 장애물
board = [list(map(int, input().split())) for _ in range(H)]

def bfs(si, sj):
    # si, sj : 위치, K : 남은 말 움직임 갯수
    q = deque()
    q.append((si, sj, 0))
    # visited[i][j][horse]
    visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 0

    while q:
        i, j, k = q.popleft()

        # 도착지점에 도착했을 때
        if i == H - 1 and j == W - 1:
            print(visited[i][j][k])
            return

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < H and 0 <= nj < W:
                if visited[ni][nj][k] == -1 and board[ni][nj] == 0:
                    q.append((ni, nj, k))
                    visited[ni][nj][k] = visited[i][j][k] + 1

        # 나이트처럼 움직일 수 있을 때
        if k + 1 <= K:
            for d in range(8):
                ni = i + di_n[d]
                nj = j + dj_n[d]

                # 인덱스 검사 & 방문 체크
                if 0 <= ni < H and 0 <= nj < W:
                    if visited[ni][nj][k + 1] == -1 and board[ni][nj] == 0:
                        # k에서 -1을 해줌
                        q.append((ni, nj, k + 1))
                        visited[ni][nj][k + 1] = visited[i][j][k] + 1

    print(-1)

bfs(0, 0)
