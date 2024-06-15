import sys

sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(y, x):

    if dp[y][x] != 0:  # 이미 계산했던곳은 바로 return
        return dp[y][x]

    move = 1  # 움직인 횟수 (처음 칸도 먹는 칸이므로 1부터 시작)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and lst[ny][nx] > lst[y][x]:
            move = max(move, dfs(ny, nx) + 1)

    dp[y][x] = move 
    return dp[y][x]


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j)) # 모든 칸 다 돌려서 찾기
print(ans)
