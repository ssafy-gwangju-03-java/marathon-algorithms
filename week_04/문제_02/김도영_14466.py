# 소가 길을 건너간 이유 6

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, K, R = map(int, input().split())

board = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

# 길 연결
for i in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    board[r1][c1].append((r2, c2))
    board[r2][c2].append((r1, c1))

cow_lst = [list(map(int, input().split())) for _ in range(K)]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    visited[si][sj] = 1

    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 1 <= ni <= N and 1 <= nj <= N:
                # 도로를 지나가지 않을 때
                if (ni, nj) not in board[i][j]:
                    # 방문하지 않았을 때
                    if visited[ni][nj] == 0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
    
    return visited

cnt = 0
for r, c in cow_lst:
    visited = bfs(r, c)
    for cow in cow_lst:
        if not visited[cow[0]][cow[1]]:
            cnt += 1

print(cnt // 2)
