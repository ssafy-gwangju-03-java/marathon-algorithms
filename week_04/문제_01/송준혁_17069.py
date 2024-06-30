# https://www.acmicpc.net/problem/17069

## Referenced
# https://www.acmicpc.net/board/view/77172

import sys

input = sys.stdin.readline
N = int(input())

# 파이프가 놓여진 방향별 (N - 1, N - 1)에서 (0, 1) 도달 가능
# 경로를 저장하기 위한 DP 배열 및 배열 초기화
dp = [[[-1] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))


def pathfinder(direction, r, c):
    """
    direction: 파이프의 방향
    현재 파이프의 끝 단 위치가 (r, c)일 때, 특정 파이프 방향에서
    도달할 수 있는 경로의 개수 반환
    """
    # 이전에 계산되었던 경로라면 결과값을 그대로 사용
    if dp[direction][r][c] != -1:
        return dp[direction][r][c]

    # 현재 위치가 벽이라면 다음 위치 진행 불가
    if grid[r][c] == 1:
        return 0

    # 가로
    if direction == 0:
        # 초기 좌표 도달 시 종료
        if c == 0:
            return 0
        # 직전 가로 좌표가 벽이면 진행 불가
        if grid[r][c - 1] == 1:
            return 0
        # 현재 위치에 가로 방향으로 놓여져 있을 경우,
        # 직전 위치에서의 파이프 방향은 가로 혹은 대각선
        # 직전 위치에서 가능한 모든 방향에서의 경로 개수 합을 DP 배열에 저장 후 반환
        dp[0][r][c] = pathfinder(0, r, c - 1) + pathfinder(2, r, c - 1)
        return dp[0][r][c]
    # 세로
    elif direction == 1:
        if r == 0:
            return 0
        # 직전 세로 좌표가 벽이면 진행 불가
        if grid[r - 1][c] == 1:
            return 0
        # 현재 위치에 세로 방향으로 놓여져 있을 경우,
        # 직전 위치에서의 파이프 방향은 세로 혹은 대각선
        dp[1][r][c] = pathfinder(1, r - 1, c) + pathfinder(2, r - 1, c)
        return dp[1][r][c]
    # 대각선
    elif direction == 2:
        if r == 0 or c == 0:
            return 0
        # 직전 대각선 좌표와 그 아래, 위 좌표가 벽이면 진행 불가
        if grid[r - 1][c] or grid[r][c - 1] or grid[r - 1][c - 1]:
            return 0
        # 현재 위치에 대각선 방향으로 놓여져 있을 경우,
        # 직전 위치에서의 파이프 방향은 가로, 세로 혹은 대각선
        dp[2][r][c] = pathfinder(0, r - 1, c - 1) + pathfinder(1, r - 1, c - 1) + pathfinder(2, r - 1, c - 1)
        return dp[2][r][c]


count = 0
# 목적지 (N - 1, N - 1)에서부터 시작, (N - 1, N - 1) 도달했을 때
# 가능한 모든 파이프 방향에서의 누적 경로 개수 계산
for i in range(3):
    count += pathfinder(i, N - 1, N - 1)

print(count)
