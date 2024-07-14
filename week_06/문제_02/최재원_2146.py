import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 대륙 번호를 저장할 3차원 배열 생성
field = [[[0, 0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        field[i][j][0] = arr[i][j]


# 3차원 배열에 대륙 번호 저장
def bfs1(i, j, idx):
    q = deque()
    q.append((i, j))
    visited1[i][j] = 1
    field[i][j][1] = idx

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and not visited1[nr][nc]:
                field[nr][nc][1] = idx
                visited1[nr][nc] = 1
                q.append((nr, nc))


visited1 = [[0] * N for _ in range(N)]
# 대륙 번호로 쓸 인덱스
continent_idx = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited1[i][j]:
            bfs1(i, j, continent_idx)
            continent_idx += 1

min_length = 200


# 대륙의 모든 지점에서 bfs -> 다른 대륙의 지점을 만날 때 까지 진행

def bfs2(i, j):
    global min_length

    q = deque()
    q.append((i, j))

    visited2 = [[0] * N for _ in range(N)]
    visited2[i][j] = 1
    idx = field[i][j][1]

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc]:
                # 다음 부분이 바다면
                if arr[nr][nc] == 0:
                    visited2[nr][nc] = visited2[r][c] + 1
                    q.append((nr, nc))
                # 다음 부분이 대륙이면
                elif arr[nr][nc] == 1:
                    # 같은 대륙이면 넘어가고 다른 대륙이면 min_value 갱신
                    if field[nr][nc][1] != idx:
                        visited2[nr][nc] = visited2[r][c] + 1
                        min_length = min(min_length, visited2[nr][nc] - 2)
                        return


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs2(i, j)

print(min_length)
