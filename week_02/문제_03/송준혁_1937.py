# https://www.acmicpc.net/problem/1937

## Referenced
# https://www.acmicpc.net/board/view/109552
# https://velog.io/@gale4739/백준-1937-욕심쟁이-판다Java

import sys

sys.setrecursionlimit(500 * 500)

input = sys.stdin.readline
n = int(input())

forest = []
for _ in range(n):
    forest.append(list(map(int, input().split())))

# 최단 거리가 아닌, 최대 거리를 구하는 것이기에 BFS보다는 DFS가 적합
# dp[r][c]: (r, c)에서 DFS 탐색 후 반환된 최대 깊이
dp = [[0] * n for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = set()


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def dfs(r, c):
    """
    DFS 탐색 순서 상, (r, c)가 이미 이전에 다른 노드에서 출발하여 방문했던 노드라면
    (r, c)에서 탐색을 시작하여 진행 가능한 깊이는 최대 (이전 방문 시 깊이 - 1)
    따라서 이미 DP 배열 상 방문 기록이 있다면 탐색하지 않음을 통해 시간 단축 가능
    """
    if dp[r][c]:
        return dp[r][c]

    # 방문한 적 없는 노드 방문 설정
    dp[r][c] = 1
    for d in direction:
        nr, nc = r + d[0], c + d[1]
        # 다음 좌표의 대나무가 더 많다면 탐색 진행
        if is_valid(nr, nc) and forest[nr][nc] > forest[r][c]:
            """
            (r, c)의 최대 깊이는 현재 깊이와 (다음 위치에서 이동 가능한 최대 깊이 + 1) 중 최대 값
            - (r, c)에서 출발하였기에 재귀 후 반환 값인 (다음 위치에서 이동 가능한 최대 깊이)에
              1을 더해야 (r, c)에서 진행 가능한 최대 깊이를 구할 수 있음
            """
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)

    # (r, c)에서 출발했을 때의 최대 탐색 깊이 반환
    return dp[r][c]


for r in range(n):
    for c in range(n):
        result.add(dfs(r, c))

print(max(result))
