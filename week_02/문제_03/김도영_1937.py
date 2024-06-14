# 욕심쟁이 판다

'''
input
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

output
4
'''
import sys
sys.setrecursionlimit(500*500)
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j):
    # 이미 계산 했을때
    if dp[i][j] != -1:
        return dp[i][j]

    # 현재 칸에 간 것 만으로도 이미 한 칸
    max_move = 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        # 0 <= ni < n and 0 <= nj < n -> 인덱스 안빠져나가고
        # bamboo[ni][nj] > bamboo[i][j] -> 다음 대나무가 지금 대나무보다 많을 때
        if 0 <= ni < n and 0 <= nj < n and bamboo[ni][nj] > bamboo[i][j]:
            max_move = max(max_move, dfs(ni, nj) + 1)
    
    dp[i][j] = max_move
    return dp[i][j]


n = int(input())

bamboo = [list(map(int, input().split())) for _ in range(n)]

# 갈 수 있는 칸 수가 0개일 수도 있으므로 -1로 초기화
dp = [[-1] * n for _ in range(n)]

result = 0
for x in range(n):
    for y in range(n):
        result = max(result, dfs(x, y))

print(result)