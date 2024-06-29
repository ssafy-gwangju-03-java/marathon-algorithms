def count_pipe(N, house):
    # 3차원 DP 배열 초기화: [행][열][파이프 방향]
    # 파이프 방향: 0-가로, 1-세로, 2-대각선
    dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
    
    # 초기 상태 설정: (0,1) 위치에 가로 방향 파이프
    dp[0][1][0] = 1
    
    # DP 배열 채우기
    for i in range(N):
        for j in range(1, N):  # 첫 번째 열 건너뛰기 (파이프의 시작점 때문)
            # 현재 위치가 벽이면 건너뛰기
            if house[i][j] == 1:
                continue
            
            # 가로 방향으로 이동
            if j > 0:
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
            
            # 세로 방향으로 이동
            if i > 0:
                dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
            
            # 대각선 방향으로 이동
            if i > 0 and j > 0 and house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
    
    # 마지막 위치에 도달하는 모든 경우의 수 더하기
    return sum(dp[N-1][N-1])

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

print(count_pipe(N, house))