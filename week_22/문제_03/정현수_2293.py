import sys
input = sys.stdin.read

lines = input().splitlines()
n, k = map(int, lines[0].split())
coins = [int(lines[i]) for i in range(1, n + 1)]

dp = [0] * (k + 1)
dp[0] = 1 

for coin in coins:
    for x in range(coin, k + 1):
        dp[x] += dp[x - coin]

print(dp[k])