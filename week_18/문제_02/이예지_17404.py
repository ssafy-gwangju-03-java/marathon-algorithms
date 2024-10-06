# 17404 RGB거리 2
import sys
input = sys.stdin.readline
maxV = 1000*1000+1

def solve(n, costs):
    ans = maxV

    # 첫 집 색상 고정하고 3번 반복
    for first in range(3):
        dp = [[maxV, maxV, maxV] for _ in range(n)]

        # 첫 집 초기화
        dp[0][first] = costs[0][first]

        # 2번째부터 마지막집까지
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        # 마지막 집
        for last in range(3):
            if last != first:
                ans = min(ans, dp[n - 1][last])

    return ans


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, costs))