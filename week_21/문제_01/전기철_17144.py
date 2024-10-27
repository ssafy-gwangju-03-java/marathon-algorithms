# 17144 미세먼지 안녕
import copy

r, c, t = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(r):
    if lst[i][0] == -1:
        clean = [i, i + 1]
        break
for _ in range(t):
    # 확산
    vis = [[0] * c for _ in range(r)]
    vis[clean[0]][0] = -1
    vis[clean[1]][0] = -1
    for i in range(r):
        for j in range(c):
            if lst[i][j] > 0:
                cnt = 0
                now = lst[i][j]
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < c and 0 <= ny < r and lst[ny][nx] != -1:
                        vis[ny][nx] += lst[i][j] // 5
                        now -= lst[i][j] // 5
                vis[i][j] += now
    # 윗바람
    start = [0, clean[0] - 1]
    dir = 0
    while True:
        x = 0
        if dir == 0:  # 상
            if start[1] == 0:
                vis[start[1]][start[0]] = vis[start[1]][start[0] + 1]
                vis[start[1]][start[0] + 1] = 0
                start[0] += 1
                dir = 1
            else:
                vis[start[1]][start[0]] = vis[start[1] - 1][start[0]]
                vis[start[1] - 1][start[0]] = 0
                start[1] -= 1
        elif dir == 1:  # 우
            if start[0] == c - 1:
                vis[start[1]][start[0]] = vis[start[1] + 1][start[0]]
                vis[start[1] + 1][start[0]] = 0
                start[1] += 1
                dir = 2
            else:
                vis[start[1]][start[0]] = vis[start[1]][start[0] + 1]
                vis[start[1]][start[0] + 1] = 0
                start[0] += 1
        elif dir == 2:  # 하
            if start[1] == clean[0]:
                vis[start[1]][start[0]] = vis[start[1]][start[0] - 1]
                vis[start[1]][start[0] - 1] = 0
                start[0] -= 1
                dir = 3
            else:
                vis[start[1]][start[0]] = vis[start[1] + 1][start[0]]
                vis[start[1] + 1][start[0]] = 0
                start[1] += 1
        else:  # 좌
            if start[0] == 1:
                break
            vis[start[1]][start[0]] = vis[start[1]][start[0] - 1]
            vis[start[1]][start[0] - 1] = 0
            start[0] -= 1

    # 아랫바람
    start = [0, clean[1] + 1]
    dir = 0
    while True:
        if dir == 0:  # 하
            if start[1] == r - 1:
                vis[start[1]][start[0]] = vis[start[1]][start[0] + 1]
                vis[start[1]][start[0] + 1] = 0
                start[0] += 1
                dir = 1
            else:
                vis[start[1]][start[0]] = vis[start[1] + 1][start[0]]
                vis[start[1] + 1][start[0]] = 0
                start[1] += 1
        elif dir == 1:  # 우
            if start[0] == c - 1:
                vis[start[1]][start[0]] = vis[start[1] - 1][start[0]]
                vis[start[1] - 1][start[0]] = 0
                start[1] -= 1
                dir = 2
            else:
                vis[start[1]][start[0]] = vis[start[1]][start[0] + 1]
                vis[start[1]][start[0] + 1] = 0
                start[0] += 1
        elif dir == 2:  # 상
            if start[1] == clean[1]:
                vis[start[1]][start[0]] = vis[start[1]][start[0] - 1]
                vis[start[1]][start[0] - 1] = 0
                start[0] -= 1
                dir = 3
            else:
                vis[start[1]][start[0]] = vis[start[1] - 1][start[0]]
                vis[start[1] - 1][start[0]] = 0
                start[1] -= 1
        else:  # 좌
            if start[0] == 1:
                break
            vis[start[1]][start[0]] = vis[start[1]][start[0] - 1]
            vis[start[1]][start[0] - 1] = 0
            start[0] -= 1
    # 복사
    lst = copy.deepcopy(vis)

# 정답
ans = 0
for i in lst:
    ans += sum(i)
    # print(i)
print(ans + 2)
