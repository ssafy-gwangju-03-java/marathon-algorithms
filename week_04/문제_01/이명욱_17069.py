# 파이프 옮기기2

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# dp[x][x][0] = 가로, dp[x][x][1] = 세로, dp[x][x][2] = 대각선
# 처음 시작 위치(가로, (0,0)->(0,1))
dp[0][1][0] = 1

for i in range(1, N):
    # 맨 왼쪽 세로줄, 이동 X
    if lst[0][i] == 1:
        break
    # 맨 위 가로줄, 가로 위치로만 이동 가능
    else:
        dp[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if not lst[i][j]:
            # 가로(가로->가로, 대각선->가로)
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        if not lst[i][j]:
            # 세로(세로->세로, 대각선->세로)
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
        if not lst[i][j - 1] and not lst[i - 1][j] and not lst[i][j]:
            # 대각선(가로-> 대각선, 세로->대각선, 대각선->대각선)
            dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

# 도착 지점
print(sum(dp[-1][-1]))