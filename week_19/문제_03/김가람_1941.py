import sys
from itertools import combinations
from collections import deque

"""
1. 25개의 좌표 중 조합으로 7개를 골라 bfs로 붙어있는지 확인
2. 7개 좌석이 전부 붙어있고 이다솜파 4명 이상이면 답 += 1
"""

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

seats = [(i // 5, i % 5) for i in range(25)]
gang = [list(sys.stdin.readline().rstrip()) for _ in range(5)]

ans = 0

for seat in combinations(seats, 7):
    q = deque()
    q.append(seat[0])
    visited = [[False] * 5 for _ in range(5)]

    while q:
        r, c = q.popleft()
        visited[r][c] = True

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if (nr, nc) in seat and not visited[nr][nc]:
                q.append((nr, nc))

    # 7개 좌표 모두 bfs로 방문하였고 'S' 4개 이상 보유했다면
    if sum([lst.count(True) for lst in visited]) == 7 and sum([int(gang[r][c] == 'S') for r, c in seat]) >= 4:
        ans += 1

print(ans)