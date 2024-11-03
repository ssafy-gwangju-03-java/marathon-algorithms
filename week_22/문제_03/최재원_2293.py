import sys
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))
coins.sort()

dp = [0] * (K + 1)
dp[0] = 1
for c in coins:
    for i in range(c, K + 1):
        dp[i] += dp[i - c]

print(dp[K])
