import sys
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(N - 1):
    a, b = arr[i]
    c = arr[i + 1][1]
    dp[i][i + 1] = a * b * c

for gap in range(2, N):
    for left in range(N - gap):
        right = left + gap

        dp[left][right] = 21e9

        for middle in range(left, right):
            dp[left][right] = min(dp[left][right], dp[left][middle] + dp[middle + 1][right]
                                  + arr[left][0] * arr[middle][1] * arr[right][1])

print(dp[0][-1])
