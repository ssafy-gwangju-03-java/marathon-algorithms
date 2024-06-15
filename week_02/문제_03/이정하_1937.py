'''
# dfs + dp 사용한 버전

import sys

sys.setrecursionlimit(500 * 500)
# 델타배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    # 1. 이미 방문한 곳은 바로 그 값 반환하기
    if memo[r][c] > 0:
        return memo[r][c]

    memo[r][c] = 1  # 현재 지점 방문 처리(자기자신)

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 범위 내에 있으면
        if 0 <= nr < N and 0 <= nc < N:
            if forest[nr][nc] > forest[r][c]:  # 전보다 대나무가 많아야 이동 가능함
                # 이동한 지점에서의 최대 이동 칸 수 계산
                now = dfs(nr, nc)
                # 현재 지점에서 이동할 수 있는 최대 칸 수 갱신하기
                memo[r][c] = now + 1 if now + 1 > memo[r][c] else memo[r][c]

    return memo[r][c]


N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
# 방문가능한 최대 칸 수 저장
memo = [[0 for _ in range(N)] for _ in range(N)]
ans = 0  # 최대 이동 칸 수
# 완탐으로 돌 것이다
for r in range(N):
    for c in range(N):
        # 각 좌표 최대 이동 칸 수 계산하기
        now_cnt = dfs(r, c)
        if ans < now_cnt:
            # 이번꺼가 현재 답보다 크먄 최대 이동 칸 수 갱신
            ans = now_cnt
print(ans)
'''

# dp만 사용한 버전

# 델타 배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 선언
# 모든 칸은 자기 자신은 방문함 => 1로 초기화
# dp[r][c] = (r, c)에서 최대한 이동 가능한 칸 수
dp = [[1 for _ in range(N)] for _ in range(N)]

# bamboo_list: 좌표와 그 좌표의 대나무 양을 함께 저장
# (대나무 양, r,c)의 묶음으로 구성
bamboo_list = [(forest[r][c], r, c) for r in range(N) for c in range(N)]

# 각 좌표에서의 대나무 양을 기준으로 오름차순 정렬
bamboo_list.sort()

# 순차적으로 DP 배열 갱신
for bamboo, r, c in bamboo_list:
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 다음 위치가 범위 내에 있고, 다음 위치의 대나무가 현재보다 많으면
        if 0 <= nr < N and 0 <= nc < N and forest[nr][nc] > forest[r][c]:
            # 최대 이동 칸 수 갱신
            dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)

# 최대 이동 칸 수 찾기
# dp배열에서 가장 큰 값!!
max_moves = max(max(row) for row in dp)

print(max_moves)
