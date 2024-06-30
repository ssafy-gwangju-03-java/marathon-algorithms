import sys
from collections import deque


N, K, R = map(int, sys.stdin.readline().split())


# 상, 하, 좌, 우
dirr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 소의 위치를 표시해 줄 배열
cow_loc = [[False] * N for _ in range(N)]

# key: 소의 좌표값, value: 소의 인덱스
cow_coords = {}

# 길을 표시해 줄 3차원 배열
# [(2, 1)] -> (2, 1)로 가는 길이 있음
road = [[[] * N for _ in range(N)] for _ in range(N)]

# 길을 건너지 않아도 만날 수 있는 소
# pair[1][2] = True -> 1번 소와 2번 소는 길을 건너지 않아도 만날 수 있음
pair = [[False] * K for _ in range(K)]


# 길이 있다면 탐색 중지
# 길을 건너지 않아도 만날 수 있는 경우만을 탐색
def bfs(r, c):
    q = deque()
    visited = [[False] * N for _ in range(N)]

    q.append((r, c))
    visited[r][c] = True

    cow_idx = cow_coords[(r, c)]

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dirr[d][0], cc + dirr[d][1]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (cr, cc) not in road[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True

                # 길을 건너지 않아도 갈 수 있는 곳에 소가 있다면 pair에 표시
                if cow_loc[nr][nc]:
                    pair_cow_idx = cow_coords[(nr, nc)]
                    pair[cow_idx][pair_cow_idx] = True
                    pair[pair_cow_idx][cow_idx] = True


# 길 입력
# (i, j)번째 원소는 (i, j)와 이어진 도착지의 좌표들의 배열
for _ in range(R):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))


# 소의 위치와 소의 인덱스를 표시
for i in range(K):
    r, c = map(int, sys.stdin.readline().split())
    cow_loc[r - 1][c - 1] = True
    cow_coords[(r - 1, c - 1)] = i


# BFS
for r, c in cow_coords.keys():
    bfs(r, c)


cnt = 0

# pair[i][j] = False -> 길을 건너지 않으면 만날 수 없음
for i in range(K):
    for j in range(i + 1, K):
        if not pair[i][j]:
            cnt += 1

print(cnt)