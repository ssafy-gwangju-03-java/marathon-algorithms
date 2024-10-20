# https://www.acmicpc.net/problem/15989

## Referenced
# https://velog.io/@dhelee/백준-15989번-123-더하기-4-Python-다이나믹-프로그래밍DP

import sys

input = sys.stdin.readline
T = int(input())

# 모든 숫자는 1을 더해서 표시 가능
dp = [1] * 10001

# 2 이상의 숫자 i가 되기 위해선 (i - 2)가 되는 방법에서
# 2를 더하는 1가지 방법을 추가하면 됨
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 3 이상의 숫자 i가 되기 위해선 (i - 3)가 되는 방법에서
# 3을 더하는 1가지 방법을 추가하면 됨
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(T):
    n = int(input())
    print(dp[n])
