# 색상환

N = int(input())
K = int(input())

# dp[i][j] : 1 ~ i번째 색 중에서 j개의 색을 선택하는 경우의 수
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 반드시 N >= 4, K >= 1
for i in range(N + 1):
    for j in range(K + 1):
        # 아무 색도 선택하지 않는 경우의 수는 1
        if j == 0:
            dp[i][j] = 1
            continue

        # i개에서 색을 1개 선택하는 경우의 수는 i
        if j == 1:
            dp[i][j] = i
            continue

        # i번째 색을 선택하지 않는 경우
        dp[i][j] += dp[i - 1][j]

        # N번째 색을 선택하는 경우
        if i == N:
            dp[i][j] += dp[i - 3][j - 1]
        else:
            dp[i][j] += dp[i - 2][j - 1]


print(dp[N][K] % 1000000003)
