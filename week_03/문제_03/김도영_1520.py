# 내리막길

'''
input
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

output
3
'''
# M : 세로, N : 가로
M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]

dm = [0, 0, 1, -1] # 세로
dn = [1, -1, 0, 0] # 가로

dp = [[-1] * N for _ in range(M)]

def dfs(m, n):
    cnt = 0

    # 목표 지점 도달
    if m == M - 1 and n == N - 1:
        return 1

    # 이미 계산 했을 경우
    if dp[m][n] != -1:
        return dp[m][n]

    for d in range(4):
        nm = m + dm[d]
        nn = n + dn[d]

        if 0 <= nm < M and 0 <= nn < N:
            if board[nm][nn] < board[m][n]:
                cnt += dfs(nm, nn)
    
    dp[m][n] = cnt
    return dp[m][n]

print(dfs(0, 0))