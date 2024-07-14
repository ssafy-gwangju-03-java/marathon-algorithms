# https://www.acmicpc.net/problem/2482

## Referenced
# https://github.com/ssafy-gwangju-03-java/marathon-algorithms/blob/main/week_06/문제_03/이명욱_2482.py

import sys

input = sys.stdin.readline
N = int(input())
K = int(input())

# DP 배열
# n개 색상 중 k개 선택할 수 있는 경우의 수: dp[k][n]
dp = [[0] * (K + 1) for _ in range(N + 1)]


def selector(N, K):
    for n in range(N + 1):
        for k in range(K + 1):
            # 색상을 고르지 않는 경우는 1가지
            if k == 0:
                dp[n][k] = 1
            # 1가지 색상 고르는 경우는 n가지
            elif k == 1:
                dp[n][k] = n
            # 마지막 인덱스 도달 X -> 원형 배열의 종료점 X
            elif n != N:
                # n개 색상 중 k개 선택하는 경우의 수 = 직전 색 선택 + 직전 색 선택 X
                # = n-1개 색상 중 k개 선택 + n-2개 색상 중 k-1개 선택
                dp[n][k] = dp[n - 1][k] + dp[n - 2][k - 1]
            # 마지막 인덱스 도달 -> 원형 배열 처음에 도착
            # 원형 배열이므로 처음 색상을 선택하지 않는 경우를 더해줌 
            else:
                dp[n][k] = dp[n - 1][k] + dp[n - 3][k - 1]

    return dp[N][K]


print(selector(N, K) % 1000000003)
