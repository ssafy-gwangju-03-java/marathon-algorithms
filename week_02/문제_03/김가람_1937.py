# 대나무 숲의 최대 크기 500 * 500으로 재귀 한도를 늘려준다
import sys
sys.setrecursionlimit(500*500)

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

# Memoization 대상 : 각 칸마다 움직일 수 있는 최댓값
# dfs하면서 이미 Memoization 된 곳은 dfs하지 않고, 아직 방문하지 않았다면 dfs하면서 Memoization
memo = [[-1] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    # 해당 칸의 움직일 수 있는 최댓값
    way = 0

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and forest[r][c] < forest[nr][nc]:
            if memo[nr][nc] == -1:
                # 4방향 중 아직 가보지않은 곳이 있다면 dfs
                way = max(way, dfs(nr, nc) + 1)
            else:
                # 이미 가본곳이라면 Memoization 된 값을 불러와 최댓값 판별
                way = max(way, memo[nr][nc] + 1)

    # 4방향 중 갈 곳 없으면 0을 리턴할 것이고 아니라면 현재 칸의 최댓값을 리턴
    memo[r][c] = way
    return memo[r][c]


for i in range(N):
    for j in range(N):
        if memo[i][j] == -1:
            dfs(i, j)

# memo 배열 원소 중 최댓값 + 1 (막힌 곳은 0부터 시작했으니까)
print(max(map(max, memo)) + 1)