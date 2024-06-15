# 욕심쟁이 판다
import sys
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    # 이미 방문한 곳이라면 dp 값 리턴(visited 역할)
    if dp[r][c]:
        return dp[r][c]
    # 방문하지 않은 곳, dp 초기값 1로 설정
    dp[r][c] = 1
    # 4 방위 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 2차원 배열 내이고 기준(r,c) 보다 주변(nr, nc)의 값이 크다면 이동
        if 0 <= nr < N and 0 <= nc < N and lst[r][c] < lst[nr][nc]:
            # 계속 이동할 수 있다면 재귀 깊어지면서 경로 끝부분 값부터 정해질 것
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    # 더 이상 이동할 수 없을 때 dp 값 리턴
    return dp[r][c]

# 입력받기
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

# 최댓값 비교
result = 0
# 2차원 배열 순회하면서 dfs
for r in range(N):
    for c in range(N):
        result = max(result, dfs(r, c))

print(result)


# 메모이제이션 제대로 작동 X, 테케만 우연히 맞은거
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# def dfs(r, c, d):
#     if dp[r][c]:
#         return
#     dp[r][c] = max(dp[r][c], d)
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if 0 <= nr < N and 0 <= nc < N and lst[r][c] < lst[nr][nc]:
#             dfs(nr, nc, d + 1)
#
#
# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * N for _ in range(N)]
#
# result = 0
# for r in range(N):
#     for c in range(N):
#         if dp[r][c] == 0:
#             dfs(r, c, 1)
#
# for r in range(N):
#     for c in range(N):
#         result = max(result, dp[r][c])
#
# print(result)