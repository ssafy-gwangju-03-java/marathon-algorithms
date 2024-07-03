# https://www.acmicpc.net/problem/13422

import sys

input = sys.stdin.readline

# 연속 M개의 합이 K 미만인 경우의 수
for T in range(int(input())):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))

    """
    # 완전탐색
    for i in range(N):
        house_sum = 0
        for j in range(i, i + M):
            if house_sum + houses[j % N] >= K:
                break
            else:
                house_sum += houses[j % N]
        else:n
            count += 1
    """

    # 초기 N개 합 구하고 순회하면서 (i - 1)번 집 빼고 (i + M)번 집 더하기
    init_sum = sum(houses[0:M])
    count = 1 if init_sum < K else 0

    # N == M일 경우 순회할 필요 없음
    if N != M:
        for i in range(1, N):
            init_sum = init_sum - houses[(i - 1) % N] + houses[(i + M - 1) % N]
            if init_sum < K:
                count += 1

    print(count)
