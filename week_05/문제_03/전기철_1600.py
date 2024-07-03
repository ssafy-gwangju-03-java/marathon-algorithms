from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
horse_dx = [-2, -2, -1, 1, 2, 2, 1, -1]
horse_dy = [-1, 1, 2, 2, 1, -1, -2, -2]
k = int(input())
w, h = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(h)]
vis = [[[-1] * (w) for _ in range(h)] for _ in range(k+1)]
vis[0][0][0] = 0


def bfs():
    q = deque()
    q.append((0, 0, 0))
    while q:
        jump, y, x = q.popleft()
        if y == h - 1 and x == w - 1:
            print(vis[jump][y][x])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if vis[jump][ny][nx] == -1 and lst[ny][nx] == 0:
                    vis[jump][ny][nx] = vis[jump][y][x] + 1
                    q.append((jump, ny, nx))
        if jump+1<=k:
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if 0 <= nx < w and 0 <= ny < h:
                    if vis[jump + 1][ny][nx] == -1 and lst[ny][nx] == 0:
                        vis[jump + 1][ny][nx] = vis[jump][y][x] + 1
                        q.append((jump + 1, ny, nx))

    print(-1)


bfs()