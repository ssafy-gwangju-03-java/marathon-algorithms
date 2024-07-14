# https://www.acmicpc.net/problem/2146

import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
islands = [[0] * N for _ in range(N)]  # 섬 인덱스용 배열
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def bfs(r, c):
    """
    섬 간 다리 탐색 함수
    - 해안가 좌표에서 시작, 바다이거나 다른 섬일 경우에만 덱에 append
    - popleft() 한 좌표가 섬이면서 출발한 섬과 다를 경우 거리 갱신
    """
    island_index = islands[r][c]
    q = deque()
    q.append((r, c, island_index))
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    distance = min_dist

    while q:
        sr, sc, si = q.popleft()

        if islands[sr][sc] != 0 and islands[sr][sc] != si:
            distance = visited[sr][sc]

        for i in range(4):
            nr, nc = sr + d[i][0], sc + d[i][1]
            if is_valid(nr, nc) and islands[nr][nc] != si and not visited[nr][nc]:
                if visited[sr][sc] + 1 >= distance:
                    break
                else:
                    visited[nr][nc] = visited[sr][sc] + 1
                    q.append((nr, nc, si))

    return distance


def islands_indexer():
    """
    grid 배열의 섬 인덱스 함수
    grid[r][c] == 1이면 탐색 진행, grid[nr][nc] == 0이면 탐색 종료 후 섬 인덱스++
    """
    visited = [[0] * N for _ in range(N)]
    count = 1

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1 and not visited[r][c]:
                q = deque()
                q.append((r, c))
                visited[r][c] = 1
                islands[r][c] = count

                while q:
                    sr, sc = q.popleft()
                    for i in range(4):
                        nr, nc = sr + d[i][0], sc + d[i][1]
                        if is_valid(nr, nc) and grid[nr][nc] and not visited[nr][nc]:
                            islands[nr][nc] = count
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                count += 1


# 최소 거리 초기화
# bfs()에서 사용한 visited 배열 특성 상 N으로 초기화 시 오탐색 발생
min_dist = 1e9
islands_indexer()

for r in range(N):
    for c in range(N):
        for i in range(4):
            nr, nc = r + d[i][0], c + d[i][1]
            # 섬의 해안가에서만 거리 탐색 진행
            if is_valid(nr, nc) and islands[r][c] and islands[nr][nc] == 0:
                min_dist = min(min_dist, bfs(r, c))
                # 해안가임이 판단되면 나머지 방향은 탐색할 필요 없음
                break

# (visited 거리 = 시작점 + 다리 길이 + 종료점) 이므로 -2
print(min_dist - 2)
