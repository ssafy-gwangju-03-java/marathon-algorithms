# https://www.acmicpc.net/problem/5549

## Referenced
# https://velog.io/@engus525/백준-5549번-행성-탐사

import sys

input = sys.stdin.readline
M, N = map(int, input().split())
K = int(input())
planet = [list(input().rstrip()) for _ in range(M)]
# 원소 누적합을 저장할 3차원 배열
# p_sum[r][c][i]: (1, 1)에서 (r, c) 좌표까지의 i 원소 누적합
p_sum = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(M + 1)]


for i in range(3):
    for r in range(1, M + 1):
        for c in range(1, N + 1):

            # (r, c)의 i 원소 누적합은 (r - 1, c), (r, c - 1) 의 누적합에
            # 중복된 (r - 1, c - 1)의 값을 제외한 값 + (r, c)의 i원소 개수
            p_sum[r][c][i] = (
                p_sum[r - 1][c][i] + p_sum[r][c - 1][i] - p_sum[r - 1][c - 1][i]
            )

            if planet[r - 1][c - 1] == "J" and i == 0:
                p_sum[r][c][i] += 1
            elif planet[r - 1][c - 1] == "O" and i == 1:
                p_sum[r][c][i] += 1
            elif planet[r - 1][c - 1] == "I" and i == 2:
                p_sum[r][c][i] += 1


for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(3):
        print(
            p_sum[c][d][i]
            - p_sum[a - 1][d][i]
            - p_sum[c][b - 1][i]
            + p_sum[a - 1][b - 1][i],
            end=" ",
        )
    print()
