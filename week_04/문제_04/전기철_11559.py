from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x, color):  # 4개 붙어있는거 찾기
    global chk
    q = deque()
    q.append((y, x))
    boom = []
    boom.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and not vis[ny][nx]:
                if lst[ny][nx] == color:  # 현재 칸 블럭과 같은 블럭이면 연결
                    vis[ny][nx] = 1
                    q.append((ny, nx))
                    boom.append([ny, nx])
    if len(boom) >= 4:  # 연결된 블럭이 4개이상이면
        for y, x in boom:  # 다 터뜨림
            lst[y][x] = "."
        chk = 1  # 터뜨렸다는 표시 (이게 0이면 끝났으므로 break)


def drop():  # 이동 (2048 문제와 비슷한 원리)
    for j in range(6):
        cnt = 11
        for i in range(11, -1, -1):
            if lst[i][j] != ".":
                x = lst[i][j]
                lst[i][j] = "."
                lst[cnt][j] = x
                cnt -= 1


lst = [list(map(str, input())) for _ in range(12)]
cnt = 0
while True:
    chk = 0
    vis = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if lst[i][j] == ".":  # 빈 공간이면 패스
                continue
            vis[i][j] = 1
            bfs(i, j, lst[i][j])  # 뿌요면 bfs 시작
    drop()  # bfs가 끝난 이후 떨어뜨리기
    if chk:  # 만약 한번 터졌으면 횟수1 추가 후 반복
        cnt += 1
    else:  # 다 끝난 상태면 break
        break
print(cnt)
