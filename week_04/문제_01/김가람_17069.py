import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 1. memo[i][j] = [1 - 가로로 놓일 수 있는 경우의 수, 2 - 대각선으로 놓일 수 있는 경우의 수, 3 - 세로로 놓일 수 있는 경우의 수]
# 2. 각 경우의 수는 파이프의 끝을 기준으로 함
# - 예: 파이프의 초기 위치는 (0, 0), (0, 1)에 [[0, 0, 0], [1, 0, 0]]로 설정
memo = [[[] for _ in range(N)] for _ in range(N)]


# 왼쪽, 왼쪽 위 대각선, 위쪽
r_dir = [0, -1, -1]
c_dir = [-1, -1, 0]


# 0열 초기값 설정
# 처음에는 파이프가 가로로 놓여져 있으므로 0열로는 움직일 수 없음
for i in range(0, N):
    memo[i][0] = [0, 0, 0]


# 0행 초기값 설정
# (0, 1) 이후로 계속 가로로 움직일 수 있으나 중간에 벽이 있으면 더이상 움직이지 못함
has_wall = False
wall_idx = 0

for i in range(1, N):
    if board[0][i]:
        has_wall = True
        wall_idx = i
        break
    memo[0][i] = [1, 0, 0]

if has_wall:
    for i in range(wall_idx, N):
        memo[0][i] = [0, 0, 0]


# 움직일 방향 d에 따라 벽의 위치를 탐색한 후 파이프를 옮길 수 있는지 알려주는 함수
# r, c == 파이프를 옮길 위치
def can_go(r, c, d):
    if d == 0 or d == 2:
        return not board[r][c]
    elif d == 1:
        return not board[r-1][c] and not board[r][c-1] and not board[r][c]


# Memoization 시작
# i, j == 파이프를 옮길 위치
for i in range(1, N):
    for j in range(1, N):
        hr, hc = i + r_dir[0], j + c_dir[0]     # 왼쪽
        dr, dc = i + r_dir[1], j + c_dir[1]     # 대각선 위쪽
        vr, vc = i + r_dir[2], j + c_dir[2]     # 위쪽

        if not (0 <= hr < N and 0 <= hc < N and can_go(i, j, 0)):
            hr, hc = 0, 0

        if not (0 <= dr < N and 0 <= dc < N and can_go(i, j, 1)):
            dr, dc = 0, 0

        if not (0 <= vr < N and 0 <= vc < N and can_go(i, j, 2)):
            vr, vc = 0, 0

        horz = memo[hr][hc][0] + memo[hr][hc][1]                        # 왼쪽에 가로, 대각선으로 놓여져 있는 파이프가 있다면 현재 칸에 가로로 놓을 수 있음
        diag = memo[dr][dc][0] + memo[dr][dc][1] + memo[dr][dc][2]      # 대각선 위쪽에 가로, 세로, 대각선으로 놓여져 있는 파이프가 있다면 현재 칸에 대각선으로 놓을 수 있음
        vert = memo[vr][vc][1] + memo[vr][vc][2]                        # 위쪽에 대각선, 세로로 놓여져 있는 파이프가 있다면 현재 칸에 세로로 놓을 수 있음

        memo[i][j] = [horz, diag, vert]


print(sum(memo[N - 1][N - 1]))