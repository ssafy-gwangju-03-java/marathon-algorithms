N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dp[N - 1][M - 1] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c):
    path = 0

    # 이미 계산된 경로가 있는 경우
    if dp[r][c] != -1:
        return dp[r][c]

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] < arr[r][c]:
            # 가능한 경로 수 누적
            path += dfs(nr, nc)

    # 누적된 경로 수 저장
    dp[r][c] = path

    return dp[r][c]


dfs(0, 0)

print(dp[0][0])
