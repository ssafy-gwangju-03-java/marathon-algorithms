# 14503 로봇청소기

a, b = map(int, input().split())
y, x, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(a)]
# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 2


# 0->3
# 1->0
# 2->1
# 3->2
def turn():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1


while True:
    chk = 0
    if lst[y][x] == 0:
        lst[y][x] = cnt
        cnt += 1
    for _ in range(4):  # 회전 후 직진
        turn()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= ny < a and 0 <= nx < b:
            if lst[ny][nx] == 0:
                x = nx
                y = ny
                chk = 1
                break
    if chk == 0:  # -> 4방향 탐색했는데 없어
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= ny < a and 0 <= nx < b:
            if lst[ny][nx] == 1:
                break
            else:
                x = nx
                y = ny
        else:
            break
print(cnt - 2)
# print(lst)
