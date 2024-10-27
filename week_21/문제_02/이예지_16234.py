# 16234 인구 이동
import sys
input = sys.stdin.readline
from collections import deque

def solve(n, l, r, people):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    day = 0
    while True:
        visited = [[False]*n for _ in range(n)] # n*n
        check = False

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    # bfs
                    Q = deque([(i, j)])
                    visited[i][j] = True
                    Q_list = [(i, j)]
                    total = people[i][j]

                    while Q:
                        x, y = Q.popleft()

                        for dx, dy in move:
                            nx = x + dx
                            ny = y + dy

                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                                gap = abs(people[x][y] - people[nx][ny])
                                if l <= gap <= r:
                                    visited[nx][ny] = True
                                    Q.append((nx, ny))
                                    Q_list.append((nx, ny))
                                    total += people[nx][ny]

                if len(Q_list) > 1: # 인구 이동 필요한 경우
                    new = total // len(Q_list)
                    for x, y in Q_list:
                        people[x][y] = new
                    check = True
        if not check:
            break
        day += 1
    return day


n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, l, r, people))