'''
# dfs 완탐 버전.. 시간초과 or 메모리초과 ㅠ
import sys
sys.setrecursionlimit(500*500*4)

# 델타배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global cnt
    if (r, c) == (M - 1, N - 1):
        cnt += 1
        return cnt

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < M and 0 <= nc < N:
            if path[nr][nc] < path[r][c]:
                dfs(nr, nc)


# 세로 M,* 가로 N
M, N = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(M)]

cnt = 0
ans = dfs(0, 0)
print(cnt)
'''
# dp
import sys

sys.setrecursionlimit(500 * 500)

# 델타배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    # 도착하면 경로 개수 1 리턴
    if (r, c) == (M - 1, N - 1):
        return 1

    # 이미 계산된 값 있으면 그 값 리턴
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0  # 현재 위치에서 시작하는 경로 개수 초기화

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if 0 <= nr < M and 0 <= nc < N:
            # 내리막길인 경우만 이동하기
            if path[nr][nc] < path[r][c]:
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]  # (r,c)에서부터의 경로 개수


# 세로 M,* 가로 N
M, N = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

ans = dfs(0, 0)
print(ans)
