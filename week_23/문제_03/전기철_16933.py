# 16933 벽 부수고 이동하기3

# 기존 벽부수고 이동하기 문제에서 day(낮) 변수 추가해서 적용

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((0, y, x, 1, 0))
    while q:
        boom, y, x, cnt, day = q.popleft()
        if x == m - 1 and y == n - 1: # 끝점 도착시 return
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if lst[ny][nx] == 1 and boom < k and not vis[boom + 1][ny][nx]: # 가는 방향이 벽이고 아직 벽 부실수 있는 상태 + 방문하지 않은 지점 
                    if day == 0: # 낮이면
                        vis[boom + 1][ny][nx] = 1 #부수고 간다
                        q.append((boom + 1, ny, nx, cnt + 1, day + 1)) 
                    else: # 밤이면
                        vis[boom][y][x] = 1  # 기다린다
                        q.append((boom, y, x, cnt + 1, (day + 1) % 2))
                elif lst[ny][nx] == 0 and not vis[boom][ny][nx]: # 벽이 아니고 평지 , 방문x
                    vis[boom][ny][nx] = 1 # 낮 밤 상관없이 간다
                    q.append((boom, ny, nx, cnt + 1, (day + 1) % 2))
    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, k = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]
vis = [[[0] * (m) for _ in range(n)] for _ in range(k + 1)]
ans = bfs(0, 0)
print(ans)
