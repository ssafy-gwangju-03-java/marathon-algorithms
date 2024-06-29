# 파이프 옮기기 2

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

# range(3)인 이유 : 가로, 세로, 대각선
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

# 초기값 설정
dp[0][0][1] = 1

for i in range(2, N):
    # 맨 윗줄
    # 가로로 밖에 못감
    if house[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, N):
    for c in range(1, N):
        # 대각선으로 다 갈 수 있는 경우
        if house[r][c] == 0 and house[r][c - 1] == 0 and house[r - 1][c] == 0:
            # 대각선 : 가로 + 세로 + 대각선
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if house[r][c] == 0:
            # 가로 : 가로 + 대각선
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            # 세로 : 세로 + 대각선
            dp[1][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

total = 0
for i in range(3):
    total += dp[i][N - 1][N - 1]

print(total)