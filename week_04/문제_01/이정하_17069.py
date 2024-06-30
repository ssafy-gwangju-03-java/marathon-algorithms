import sys

sys.setrecursionlimit(10 ** 5)

# 입력 최대값
max_input = 32 + 1
# 방향 3가지 - 우 우하 하
max_dir = 3
# 델타배열
dr = [0, 1, 1]
dc = [1, 1, 0]

dp = [[[-1] * max_dir for _ in range(max_input)] for _ in range(max_input)]
home = [[0] * max_input for _ in range(max_input)]


# 현재 위치, 방향 따라 이동 가능 여부 체크
def ok(r, c, dir):
    if dir == 0:  # 진행하려는 방향이 가로일 때 가능한 공간 체크
        for k in range(1):
            nr = r + dr[k]
            nc = c + dc[k]
            if not (1 <= nr <= N and 1 <= nc <= N and home[nr][nc] == 0):
                return False
    elif dir == 1:  # 대각선일 때 가능한 공간 체크
        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if not (1 <= nr <= N and 1 <= nc <= N and home[nr][nc] == 0):
                return False
    elif dir == 2:  # 세로일 때
        for k in range(2, 3):
            nr = r + dr[k]
            nc = c + dc[k]
            if not (1 <= nr <= N and 1 <= nc <= N and home[nr][nc] == 0):
                return False
    return True


# 경로 수 계산하기
def dfs(r, c, dir):
    if r == N and c == N:
        return 1  # 목적지 도착하면 카운트++

    if dp[r][c][dir] != -1:
        return dp[r][c][dir]  # 이미 계산된 경로 수 있으면 중복 계산 x

    dp[r][c][dir] = 0  # 새로 경로 수를 계산하려면 초기화 해야 함

    if dir == 0:  # 진행 중인 방향이 가로일 때
        for k in range(2):
            if ok(r, c, k):
                dp[r][c][dir] += dfs(r + dr[k], c + dc[k], k)
    elif dir == 1:  # 대각선일 때
        for k in range(3):
            if ok(r, c, k):
                dp[r][c][dir] += dfs(r + dr[k], c + dc[k], k)
    elif dir == 2:  # 세로 방향
        for k in range(1, 3):
            if ok(r, c, k):
                dp[r][c][dir] += dfs(r + dr[k], c + dc[k], k)

    return dp[r][c][dir]


N = int(input())

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        home[i + 1][j + 1] = row[j]

# dp 배열 초기화
for i in range(max_input):
    for j in range(max_input):
        for k in range(max_dir):
            dp[i][j][k] = -1

# (1,2)에서 시작해서 0 방향(우측)으로 이동
print(dfs(1, 2, 0))