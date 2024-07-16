import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]


# 빙산 내륙을 BFS
# 리턴 : border = [(행, 열, 주변 얼음의 갯수) if 경계값]
def bfs(r, c, visited):
    visited[r][c] = True
    q = deque()
    q.append((r, c))

    border = []

    while q:
        cr, cc = q.popleft()
        ice = 0

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and sea[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                elif not sea[nr][nc]:
                    ice += 1

        if ice:
            border.append((cr, cc, ice))

    return border


def melt():
    year = 0

    while True:
        did_bfs = False
        visited = [[False] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):

                # 방문하지 않은 빙산이 있다면 BFS
                if sea[i][j] and not visited[i][j]:
                    if not did_bfs:
                        border = bfs(i, j, visited)
                        did_bfs = True

                        # BFS가 리턴한 경계값들을 한번에 녹여주기
                        for r, c, ice in border:
                            sea[r][c] -= ice
                            if sea[r][c] < 0:
                                sea[r][c] = 0

                    # 이미 BFS가 끝났는데 아직 방문하지 않은 빙산이 있다면 분리된 것이므로 return
                    else:
                        return year

        year += 1

        # 지도를 전부 순회했는데 BFS를 수행할 빙산이 없다면 이미 다 녹은 것이므로 리턴 0
        if not did_bfs:
            return 0


print(melt())