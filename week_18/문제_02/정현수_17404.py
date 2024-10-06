N = int(input())
house_rgb = [list(map(int, input().split())) for _ in range(N)]

INF = 10e8
ans = INF  #

# 첫 번째 집을 R, G, B로 색칠했을 때 각각의 경우에 대해 계산
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]

    # 첫 번째 집: i번째 색
    dp[0][i] = house_rgb[0][i]

    # 두 번째 집부터 N번째 집까지 색칠
    for j in range(1, N):
        dp[j][0] = house_rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])  # R로 색칠할 때
        dp[j][1] = house_rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])  # G로 색칠할 때
        dp[j][2] = house_rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])  # B로 색칠할 때

    # 마지막 집의 색이 첫 번째 집의 색과 다를 때만 최솟값을 선택
    for c in range(3):
        if i != c:  # 첫 번째 집과 마지막 집의 색이 다를 때만 선택
            ans = min(ans, dp[-1][c])

print(int(ans))
