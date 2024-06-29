import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c][d]는 방향 d로 (r, c)에 도달하는 경우의 수
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 시작 위치
dp[0][1][0] = 1

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            continue

        # 가로 방향
        if c > 0 and arr[r][c - 1] == 0:
            dp[r][c][0] += dp[r][c - 1][0]
            dp[r][c][0] += dp[r][c - 1][2]

        # 세로 방향
        if r > 0 and arr[r - 1][c] == 0:
            dp[r][c][1] += dp[r - 1][c][1]
            dp[r][c][1] += dp[r - 1][c][2]

        # 대각선 방향
        if r > 0 and c > 0 and arr[r - 1][c] == 0 and arr[r][c - 1] == 0 and arr[r - 1][c - 1] == 0:
            dp[r][c][2] += dp[r - 1][c - 1][0]
            dp[r][c][2] += dp[r - 1][c - 1][1]
            dp[r][c][2] += dp[r - 1][c - 1][2]

# 오른쪽 아래 코너에 도달하는 모든 방법의 합
answer = dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]

print(answer)