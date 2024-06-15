def calculate_max_score():
    # 초기화 / i번째 이동 후 j번째 칸에 있을 때 최대 점수
    INF = -10001
    dp = [[INF] * (N + 1) for _ in range(T)]

    # 초기 점수 설정
    for i in range(S):
        dp[0][i] = board[i]

    # DP 테이블 채우기
    for i in range(T - 1):
        for j in range(N):
            # 유효한 위치인지 확인
            if dp[i][j] != INF:
                for k in range(1, S + 1):
                    # 마지막 칸을 넘는 경우
                    if j + k >= N:
                        dp[i + 1][N] = max(dp[i + 1][N], dp[i][j])
                    # 정확히 도착하는 경우
                    else:
                        dp[i + 1][j + k] = max(dp[i + 1][j + k], dp[i][j] + board[j + k])

    # 마지막 이동 후 마지막 칸에 도달했을 때의 최대 점수
    return dp[-1][-1]


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    N, S, T = arr[0], arr[1], arr[2]

    board = []
    while len(board) < N:
        board.extend(list(map(int, input().split())))

    result = calculate_max_score()

    print(result)
