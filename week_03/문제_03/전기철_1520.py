dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    cnt = 0
    if dp[y][x] != -1:
        return dp[y][x]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if lst[ny][nx] < lst[y][x]:
                cnt += dfs(nx, ny)
    dp[y][x] = cnt
    return dp[y][x]


m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dp[m - 1][n - 1] = 1
print(dfs(0, 0))
