import sys
input = sys.stdin.readline
def recur(n, w):
    if w > K:
        return -999999
    if n == N:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]
    
    dp[n][w] = max(recur(n+1, w+arr[n][0]) + arr[n][1], recur(n+1, w))
    return dp[n][w]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100001)] for _ in range(N)]

ans = recur(0, 0)

print(ans)