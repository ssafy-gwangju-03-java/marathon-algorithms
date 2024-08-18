import sys

sys.stdin = open("../../input.txt", 'r')

input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

while len(scv) < 3:
    scv.append(0)


def dfs(x, y, z):
    if (x, y, z) == (0, 0, 0):
        return 0

    if dp[x][y][z]:
        return dp[x][y][z]

    dp[x][y][z] = 1 + min(dfs(max(x - 9, 0), max(y - 3, 0), max(z - 1, 0)),
                          dfs(max(x - 9, 0), max(y - 1, 0), max(z - 3, 0)),
                          dfs(max(x - 3, 0), max(y - 9, 0), max(z - 1, 0)),
                          dfs(max(x - 3, 0), max(y - 1, 0), max(z - 9, 0)),
                          dfs(max(x - 1, 0), max(y - 3, 0), max(z - 9, 0)),
                          dfs(max(x - 1, 0), max(y - 9, 0), max(z - 3, 0)))

    return dp[x][y][z]


print(dfs(scv[0], scv[1], scv[2]))
