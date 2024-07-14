N = int(input())
K = int(input())

# dp[i][j] : i개의 색 중에서 j개의 색을 선택하는 경우의 수
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(K + 1):
        # 초기값 세팅
        # 색을 고르지 않는 경우
        if j == 0:
            dp[i][j] = 1
            continue
        # 색을 1개만 고르는 경우
        if j == 1:
            dp[i][j] = i
            continue
        # i번째 색을 포함시키지 않고 j개의 색 선택
        dp[i][j] += dp[i-1][j]
        # i번째 색을 포함시키고 j개의 색을 선택
        if i != N:
            dp[i][j] += dp[i-2][j-1]
        # i가 마지막인 N번째 색을 포함할 경우 첫번째 색을 사용 하지 못하는 조건 추가(원형이기 때문)
        else:
            dp[i][j] += dp[i-3][j-1]

print(dp[N][K] % 1000000003)