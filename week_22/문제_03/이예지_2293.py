# 2293 동전 1

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp[i]: i원을 만들 수 있는 경우
dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만드는 경우는 1가지

for coin in coins:
    for i in range(coin, k + 1):  # coin원 ~ k원
        dp[i] += dp[i - coin]

print(dp[k])