# 빙산
from collections import deque

# 빙산 덩어리 분리된 개수 찾기
def bfs(sr, sc):
    visited[sr][sc] = 1
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            # 빙산 범위내이며 바다 부분이 아니고 방문하지 않은 곳일때 이동
            if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] != 0 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1

# 빙산 녹이기
def melt():
    melt_lst = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if lst[r][c] > 0:
                count = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    # 주변 바다의 개수 세기
                    if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0:
                        count += 1
                melt_lst[r][c] = count
    # 주변 바다의 개수 만큼 원래 빙산에서 빼주기
    for r in range(N):
        for c in range(M):
            # 최소값 0 보정
            lst[r][c] = max(lst[r][c] - melt_lst[r][c], 0)

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

years = 0
while True:
    visited = [[0] * M for _ in range(N)]
    land = 0
    # 덩어리 세기
    for sr in range(N):
        for sc in range(M):
            if lst[sr][sc] != 0 and visited[sr][sc] == 0:
                bfs(sr, sc)
                land += 1
    # 빙산이 다 녹을 때까지 분리 되지 않으면 0
    if land == 0:
        print(0)
        break
    if land >= 2:
        print(years)
        break
    # 덩어리가 1개라면 녹이고 1년 증가
    melt()
    years += 1
