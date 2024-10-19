# 15989 1,2,3 더하기 4
dp = [i for i in range(10001)]
# 1,7,13 -> 6n+1마다 다르게 더해지고 나머지는 동일
for i in range(2, 10001):
    if i % 6 == 1:
        dp[i] = dp[i - 1] + (i // 6)
    else:
        dp[i] = dp[i - 1] + (i // 6 + 1)

n = int(input())
for _ in range(n):
    a = int(input())
    print(dp[a])
