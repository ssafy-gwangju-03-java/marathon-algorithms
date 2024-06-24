import sys

input = sys.stdin.readline
a = int(input())
lst = [[0] * (a + 1)]
for _ in range(a):
    b = [0] + list(map(int, input().split()))
    lst.append(b)

dp = [[[0, 0, 0] for _ in range(a + 1)] for _ in range(a + 1)]  # 가로 세로 대각
dp[1][2][0] = 1  # (1,2)에 가로로 배치되어있으므로 (1,2,0)=1

for y in range(1, a + 1):
    for x in range(3, a + 1):
        if lst[y][x] == 0:
            dp[y][x][0] = (
                dp[y][x - 1][0] + dp[y][x - 1][2]
            )  # 가로진행 -> 이전칸의 가로+대각
            dp[y][x][1] = (
                dp[y - 1][x][1] + dp[y - 1][x][2]
            )  # 세로진행 -> 이전칸의 세로+대각
            if (
                lst[y - 1][x] == 1 or lst[y][x - 1] == 1
            ):  # 대각진행의 경우 왼쪽,위에 벽이있으면 0으로 초기화
                dp[y][x][2] = 0
            else:  # 벽이 없는경우 왼쪽 위 칸의 가로 세로 대각을 합한 경우의 수와 같음
                dp[y][x][2] = (
                    dp[y - 1][x - 1][0] + dp[y - 1][x - 1][1] + dp[y - 1][x - 1][2]
                )
        else:  # 벽인 경우 0 0 0으로 초기화
            dp[y][x] = [0, 0, 0]
print(sum(dp[y][x]))
