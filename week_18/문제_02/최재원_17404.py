import sys

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_v = 1_000_000

for i in range(3):
    dp = [[1000] * 3 for _ in range(N)]
    # 첫 번째 집의 색만 선택
    dp[0][i] = arr[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + arr[j][0]  # 삘간색 0
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + arr[j][1]  # 초록색 1
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + arr[j][2]  # 파란색 2

    dp[-1][i] = 1_000_000  # 첫번째 집과 같은 색 거르기
    min_v = min(min_v, min(dp[-1]))

print(min_v)
