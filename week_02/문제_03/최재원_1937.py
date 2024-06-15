import sys
sys.stdin = open("../input.txt")

sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(x, y):
    # 방문한 적이 있으면 그 값 사용
    if dp[x][y]:
        return dp[x][y]

    # 방문한 적이 없으면 1부터 시작
    dp[x][y] = 1

    for d in range(4):
        nx = x + dr[d]
        ny = y + dc[d]

        # 숫자가 더 큰 곳이 있으면
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            # 최대 길이 선택
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)