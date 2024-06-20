import sys
sys.setrecursionlimit(500*500)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
memo = [[-1] * C for _ in range(R)]


# 2주차 욕심쟁이 판다와 같은 방법의 풀이
def dfs(r, c):

    # 시작점에 도달했을 시에만 1을 리턴
    if r == 0 and c == 0:
        return 1

    if memo[r][c] != -1:
        return memo[r][c]

    way = 0

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] > board[r][c]:
            way += dfs(nr, nc)

    memo[r][c] = way
    return way

dfs(R-1, C-1)
print(memo[R-1][C-1])