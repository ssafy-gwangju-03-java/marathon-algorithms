# 행성 탐사

import sys
input = sys.stdin.readline
from pprint import pprint

N, M = map(int, input().split())
K = int(input())

# 행성의 정보를 저장할 리스트
# 정글 : J
# 바다 : O
# 얼음 : I
planet = [list(input()) for _ in range(N)]

# 행성 정보마다의 누적합 배열
# 정글
jungle = [[0] * (M + 1) for _ in range(N + 1)]

# 바다
ocean = [[0] * (M + 1) for _ in range(N + 1)]

# 얼음
ice = [[0] * (M + 1) for _ in range(N + 1)]

# 누적합 구하기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        jungle[i][j] = jungle[i - 1][j] + jungle[i][j - 1] - jungle[i - 1][j - 1]
        ocean[i][j] = ocean[i - 1][j] + ocean[i][j - 1] - ocean[i - 1][j - 1]
        ice[i][j] = ice[i - 1][j] + ice[i][j - 1] - ice[i - 1][j - 1]

        if planet[i - 1][j - 1] == "J":
            jungle[i][j] += 1

        elif planet[i - 1][j - 1] == "O":
            ocean[i][j] += 1

        elif planet[i - 1][j - 1] == "I":
            ice[i][j] += 1

for _ in range(K):
    a, b, c, d = map(int, input().split())

    # 누적합을 이용하여 구간합 구하기
    j = jungle[c][d] - jungle[a - 1][d] - jungle[c][b - 1] + jungle[a - 1][b - 1]
    o = ocean[c][d] - ocean[a - 1][d] - ocean[c][b - 1] + ocean[a - 1][b - 1]
    i = ice[c][d] - ice[a - 1][d] - ice[c][b - 1] + ice[a - 1][b - 1]

    print(j, o, i)
