# 17144 미세먼지 안녕!
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]

# 1. 확산 (//5)
def spread():
    # 현재 상태 복사(확산 한번에!!!)
    temp = [[0]*c for _ in range(r)]

    for row in range(r):
        for col in range(c):
            if maps[row][col] > 0:  # 미세먼지가 있어야 확산이 되지!
                part = maps[row][col] // 5
                cnt = 0
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < r and 0 <= nc < c and maps[nr][nc] != -1:
                        temp[nr][nc] += part
                        cnt += 1
                # 원래 위치(row, col)의 미세먼지 양
                temp[row][col] += maps[row][col] - (part * cnt)

    # 공기청정기 위치는 그대로!!
    for i in range(r):
        for j in range(c):
            if maps[i][0] == -1:
                temp[i][0] = -1

    return temp

# 2. 공기청정기 작동 --> 밀기 아니고 당기기여야 함....ㅠㅠ
def clean():
    # 공기청정기 찾기
    up = -1
    for i in range(r):
        if maps[i][0] == -1:
            up = i
            break
    down = up + 1   # 밑으로 돌거는 바로 아래니까
    # 위로(반시계)
    for i in range(up - 1, 0, -1):  # 위로 당기기
        maps[i][0] = maps[i - 1][0]
    for i in range(0, c - 1):  # 왼쪽으로 당기기
        maps[0][i] = maps[0][i + 1]
    for i in range(0, up):  # 아래로 당기기
        maps[i][c - 1] = maps[i + 1][c - 1]
    for i in range(c - 1, 1, -1):  # 오른쪽으로 당기기
        maps[up][i] = maps[up][i - 1]

    # 아래로(시계)
    for i in range(down+1, r-1):    # 아래로 당기기
        maps[i][0] = maps[i+1][0]
    for i in range(0, c-1):         # 왼쪽으로 당기기
        maps[r-1][i] = maps[r-1][i+1]
    for i in range(r-1, down, -1):  # 위로 당기기
        maps[i][c-1] = maps[i-1][c-1]
    for i in range(c-1, 1, -1):     # 오른쪽으로 당기기
        maps[down][i] = maps[down][i-1]
    # 청소
    maps[up][1] = 0
    maps[down][1] = 0


# 3. 남아있는 미세먼지 양(sum?)
def solve():
    global maps
    for _ in range(t):
       maps = spread()
       clean()

    total = 0
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                total += maps[i][j]
    return total

print(solve())