import sys

"""
부동 소수점 오차
https://velog.io/@syleemk/CS-%EB%B6%80%EB%8F%99-%EC%86%8C%EC%88%98%EC%A0%90-%EC%98%A4%EC%B0%A8
"""

while True:
    N, M = sys.stdin.readline().split()
    N = int(N)
    M = int(float(M) * 100 + 0.5)
    if not N and not M:
        break

    # 1차원 Knapsack (2차원으로 하면 메모리초과)
    memo = [0] * (M + 1)
    cal = []

    for _ in range(N):
        C, P = sys.stdin.readline().split()
        C = int(C)
        P = int(float(P) * 100 + 0.5)
        cal.append((P, C))

    cal.sort(key=lambda x: x[0])

    for i in range(N):
        for j in range(1, M + 1):
            if j >= cal[i][0]:
                memo[j] = max(memo[j], memo[j - cal[i][0]] + cal[i][1])

    print(memo[M])
