import sys
from collections import deque

N, T = map(int, input().split())
maps = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N ** 2):
    x = i // N
    y = i % N
    a, b, c, d = map(int, input().split(" "))
    maps[x][y] = [a, b, c, d]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
signal = {
    1: [0, 1, 3],
    2: [0, 1, 2],
    3: [1, 2, 3],
    4: [0, 2, 3],
    5: [0, 1],
    6: [1, 2],
    7: [2, 3],
    8: [0, 3],
    9: [0, 3],
    10: [0, 1],
    11: [1, 2],
    12: [2, 3]

}

visited = set()
visited.add((0, 0))

q = deque()
q.append((0, 0, 1, 0))

while q:

    x, y, nd, cnt = q.popleft()

    if cnt == T:
        continue

    now_time = cnt % 4
    now_signal = maps[x][y][now_time]
    # print(x,y,nd,cnt,now_signal)
    # 현재 방향에 따라 교차로 진입여부 설정
    if nd == 0:
        if now_signal in (1, 5, 9):
            pos = signal[now_signal]
            for go in pos:
                nx = x + dx[go]
                ny = y + dy[go]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny, go, cnt + 1))
    elif nd == 1:
        if now_signal in (2, 6, 10):
            pos = signal[now_signal]
            for go in pos:
                nx = x + dx[go]
                ny = y + dy[go]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny, go, cnt + 1))
    elif nd == 2:
        if now_signal in (3, 7, 11):

            pos = signal[now_signal]
            for go in pos:
                nx = x + dx[go]
                ny = y + dy[go]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny, go, cnt + 1))

    elif nd == 3:
        if now_signal in (4, 8, 12):
            pos = signal[now_signal]
            for go in pos:
                nx = x + dx[go]
                ny = y + dy[go]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny, go, cnt + 1))

print(len(visited))

# 참고: https://door-of-tabris.tistory.com