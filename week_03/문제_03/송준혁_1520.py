# https://www.acmicpc.net/problem/1520

## Referenced
# https://www.acmicpc.net/board/view/128488

import sys

sys.setrecursionlimit(500 * 500)

input = sys.stdin.readline
M, N = map(int, input().split())
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

grid = []
for _ in range(M):
    grid.append(list(map(int, input().split())))

# DP 배열 초기화
# dp[r][c]: (r, c)에서 (N - 1, M - 1)로 도달할 수 있는 경로의 개수
# DP 경로 계산 결과가 0이어도 중복 연산이 이루어지지 않도록 -1로 초기화
# https://www.acmicpc.net/board/view/139826
# https://www.acmicpc.net/board/view/139826
dp = [[-1] * N for _ in range(M)]


def pathfinder(r, c):

    def is_valid(r, c):
        return 0 <= r < M and 0 <= c < N

    # DP 배열에 걸리지 않고 처음으로 (N - 1, M - 1)에 도달한 경로일 경우
    if r == M - 1 and c == N - 1:
        return 1

    # 이전 DFS 탐색에서 지나갔던 길은 결국 (N - 1, M - 1)에 도달하는 경로
    # 그 좌표에서 (N - 1, M - 1)에 도달할 수 있는 경로 개수를 반환
    if dp[r][c] != -1:
        return dp[r][c]

    count = 0
    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if is_valid(nr, nc) and grid[nr][nc] < grid[r][c]:
            """
            현재 좌표 (r, c)에서 (N - 1, M - 1)에 도달할 수 있는 경로는
            4방위 DFS 탐색 후 얻은 각 방향의 경로 개수의 누적합
            """
            count += pathfinder(nr, nc)

    # 현재 좌표의 누적 경로 개수를 반환
    dp[r][c] = count
    return count


print(pathfinder(0, 0))
