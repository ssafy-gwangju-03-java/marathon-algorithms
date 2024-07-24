# 12856 평범한 배낭

n, k = map(int, input().split())
bag = [(0, 0)]  # 헷갈리지 않게 idx 1번부터 시작하려고 (0,0) 넣음
for i in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]  # dp[n][m] = n개의 물건으로 m 무게 이하로 가능한 최대 가중치

for i in range(1, n + 1):  # 물건 개수
    w, v = bag[i]
    for j in range(1, k + 1):  # 물건 무게
        if j - w < 0:  # 가방 하중보다 물건이 무거워서 못넣음
            dp[i][j] = dp[i - 1][j]  # 이전 물건 안넣은거랑 가중치 동일 (물건 안넣음)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)  # 물건 안넣는 케이스(dp[i-1][j]), 물건 넣는 케이스(dp[i-1][j-w]+v) 비교

print(dp[n][k])
