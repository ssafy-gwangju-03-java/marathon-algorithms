# https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline
N, K = map(int, input().split())

# 무게 K일 때의 가치의 최대값을 저장할 DP 배열
dp = [0] * (K + 1)
goods = []

for _ in range(N):
    W, V = map(int, input().split())
    goods.append((W, V))

for W, V in goods:
    # 무게 W ~ K 까지 확인
    for j in range(K, W - 1, -1):
        # 특정 무게 j에서의 가치:
        # 기존 저장된 가치와 물건을 넣었을 경우 가치 중 최대값
        dp[j] = max(dp[j], dp[j - W] + V)

print(dp[-1])
