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
# dp+dfs
import sys

sys.setrecursionlimit(100000)
# 500*500*4가 이론적으로 최대 탐색횟수인데, 500*500정도로 크게 하면 무조건 메모리초과 남
# 재귀 호출 스택의 메모리 사용 때문.
# 이론적으로 250000개의 함수 호출 스택을 유지해야 한다는 소리.
# dfs 완탐은 10만번으로는 시초 남.
# 결국 100000번 안에 탐색할수있는 dfs+dp 조합으로 가야하는 것!

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
