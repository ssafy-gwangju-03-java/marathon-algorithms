# https://www.acmicpc.net/problem/16234

import sys
from collections import deque

input = sys.stdin.readline


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def union_finder(r, c, visited):
    # BFS 탐색으로 연합 생성
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    union = [(r, c)]
    people = [nations[r][c]]

    while q:
        sr, sc = q.popleft()

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if (
                is_valid(nr, nc)
                and not visited[nr][nc]
                and L <= abs(nations[sr][sc] - nations[nr][nc]) <= R
            ):
                union.append((nr, nc))
                people.append(nations[nr][nc])
                q.append((nr, nc))
                visited[nr][nc] = 1

    # 연합이 만들어졌다면, 평균 인구수로 인구 이동
    if len(union) > 1:
        count = sum(people) // len(union)
        for nation in union:
            tr, tc = nation
            nations[tr][tc] = count
        return True

    return False


N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
count = 0

while True:
    # 연합은 지도 곳곳에 생성될 수 있으므로, 방문 배열은 반복문 전역에서 사용
    visited = [[0] * N for _ in range(N)]
    has_moved = False

    for r in range(N):
        for c in range(N):
            if not visited[r][c] and union_finder(r, c, visited):
                has_moved = True

    if has_moved:
        count += 1
    else:
        break

print(count)
