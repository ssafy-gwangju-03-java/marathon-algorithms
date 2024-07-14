import sys
from collections import deque

N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 섬들을 구분지어서 표시해 줄 새로운 지도
# 1번째 섬은 1로, 2번째 섬은 2로, ... N번째 섬은 N으로 표시
island = [[0] * N for _ in range(N)]

# 섬의 숫자를 표시해 줄 BFS 함수
# BFS가 끝나면 바다와 닿아있는 경계(border)의 좌표를 반환
def divide_island_bfs(r, c, island_num):
    q = deque()
    q.append((r, c))
    island[r][c] = island_num

    border = set()

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N:

                # 원본 배열 sea에 섬이 존재하고 새 배열 island에 아직 표시가 안되어있다면
                if sea[nr][nc] and not island[nr][nc]:
                    island[nr][nc] = island_num
                    q.append((nr, nc))

                # 바다(0)와 맞닿아 있다면 현재 좌표값을 border에 추가
                elif not sea[nr][nc]:
                    border.add((cr, cc))

    return list(border)


# 다리를 건설할 BFS 함수
# 현재 섬과 다른 섬에 닿는 순간 이동 횟수를 return
def build_bridge_bfs(border, island_num):
    visited = [[False] * N for _ in range(N)]
    q = deque(border)

    for coords in border:
        visited[coords[0]][coords[1]] = True

    turn = 0

    while q:
        q_size = len(q)

        for _ in range(q_size):
            cr, cc = q.popleft()

            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if island[nr][nc]:
                        # 현재 섬의 육지를 만나면 continue, 다리는 바다에만 놓는다
                        if island[nr][nc] == island_num:
                            continue
                        # 다른 섬의 육지를 만나면 다리가 놓아진 것이므로 return
                        else:
                            return turn
                    visited[nr][nc] = True
                    q.append((nr, nc))

        turn += 1


island_cnt = 0
borders = []

# 섬 숫자 표시
for i in range(N):
    for j in range(N):
        if sea[i][j] and not island[i][j]:
            island_cnt += 1
            border = divide_island_bfs(i, j, island_cnt)
            borders.append(border)

min_bridge = 10000

# 완전탐색
for i, border in enumerate(borders):
    min_bridge = min(min_bridge, build_bridge_bfs(border, i + 1))

print(min_bridge)