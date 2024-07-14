import sys

def dp(n, k):
    # 20개 색상환에서 11개 이상의 색을 선택할 수는 없음
    if n / k < 2:
        return 0

    # 20개 색상환에서 10개의 색을 선택하는 경우의 수는 2
    if n / k == 2:
        return 2

    # 20개 색상환에서 1개의 색을 선택하는 경우의 수는 20
    if k == 1:
        return n

    # 어떠한 색도 뽑지 않는 경우의 수는 0
    if k <= 0:
        return 1

    # 계산해놓은 경우의 수가 있다면 return
    if memo[n][k]:
        return memo[n][k]

    # dp(n - 1, k) == N번째 색을 선택하지 않는 경우 == N - 1개의 색만 뽑는 경우
    # dp(n - 2, k - 1) == N번째 색을 선택하는 경우 == N - 2개의 색 뽑은 후 N번째 색 뽑아주기
    memo[n][k] = dp(n - 1, k) + dp(n - 2, k - 1)

    return memo[n][k]


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# N개의 색 중 K개를 뽑는 경우의 수
memo = [[0] * (K + 1) for _ in range(N + 1)]
print(dp(N, K) % 1000000003)







