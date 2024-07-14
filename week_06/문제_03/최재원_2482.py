import sys
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = int(input())
K = int(input())

def dp(n, k):
    if n / k < 2:
        return 0

    # 절반을 선택하는 경우의 수 2
    if n / k == 2:
        return 2

    # 남은 n색상환 중 1개를 선택하는 경우의 수 n
    if k == 1:
        return n

    # 다 뽑은 경우의 수 1
    if k == 0:
        return 1

    # 계산해놓은 경우의 수가 있다면 return
    if memo[n][k]:
        return memo[n][k]

    # dp(n - 1, k) == N번째 색을 선택하지 않는 경우 색상환 선택지 1 줄이기
    # dp(n - 2, k - 1) == N번째 색을 선택하는 경우 색상환 선택지 2개 줄이고 뽑아야 하는 수 1개 줄이기
    memo[n][k] = dp(n - 1, k) + dp(n - 2, k - 1)

    return memo[n][k]


# memo[n][k] -> n색상환에서 k개를 뽑는 경우의 수
memo = [[0] * (K + 1) for _ in range(N + 1)]
print(dp(N, K) % 1000000003)
