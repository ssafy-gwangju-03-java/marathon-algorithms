import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# need_visit[방문해야 할 좌표] = 해당 좌표를 방문해야 할 순서
need_visit = {}
for i in range(1, M + 1):
    r, c = map(int, sys.stdin.readline().split())
    need_visit[(r - 1, c - 1)] = i


def dfs(r, c, visited, next_stop):
    global ans
    should_stop = need_visit.get((r, c), None)

    if should_stop:
        if should_stop != next_stop:    # 방문해야 하는 좌표에 도달했으나 순서가 맞지 않으면 return
            return
        else:
            if next_stop == M:
                ans += 1
                return
            next_stop += 1

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not grid[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, visited, next_stop)
            visited[nr][nc] = False


# 시작점
sr, sc = 0, 0

for k, v in need_visit.items():
    if v == 1:
        sr, sc = k

visited = [[False] * N for _ in range(N)]
visited[sr][sc] = 1

ans = 0
dfs(sr, sc, visited, 1)
print(ans)


