N = int(input())

dp = [[0] * (N + 2) for _ in range(3)]
dp[0][2] = dp[1][2] = 1

for i in range(3, N + 1):
    dp[0][i] = dp[1][i - 1] + dp[2][i - 1]
    dp[1][i] = dp[0][i - 1] + dp[2][i - 1]
    dp[2][i] = dp[0][i - 1] + dp[1][i - 1]

print(dp[0][N] % 1_000_000_007)
