import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))

# 인덱스 무게에서의 최대 가치를 저장
dp = [0] * (K + 1)

for W, V in arr:
    for j in range(K, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + V)
        print(dp)

print(dp[K])
