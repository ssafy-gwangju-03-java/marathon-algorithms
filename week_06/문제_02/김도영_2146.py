# 다리 만들기

import sys
sys.setrecursionlimit(500*500)
from collections import deque

input = sys.stdin.readline

N = int(input())
# 0 : 바다, 1 : 섬
board = [list(map(int, input().split())) for _ in range(N)]

result = 1e9
land = 2

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]


# 섬 번호 붙이기
def bfs(land_num):
    global result
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if board[i][j] == land_num:
                q.append((i, j))
                visited[i][j] = 0

    while q:
        i, j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 인덱스 검사
            if 0 <= ni < N and 0 <= nj < N:
                # 다른 섬에 도착한 경우
                if board[ni][nj] > 0 and board[ni][nj] != land_num:
                    result = min(result, visited[i][j])
                    return

                # 바다인 경우
                if board[ni][nj] == 0 and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))

def dfs(i, j):
    global land
    if not (0 <= i < N and 0 <= j < N):
        return False
    
    if board[i][j] == 1:
        board[i][j] = land
        
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            dfs(ni, nj)
        
        return True

    return False
    
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            land += 1

for i in range(2, land):
    bfs(i)

print(result)