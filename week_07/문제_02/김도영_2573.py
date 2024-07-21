import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 빙산의 초기 상태
graph = []
index = 2
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    index += M

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 빙산의 덩어리 개수 세기
def bfs(si, sj, visited):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni = i + di[d] 
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and graph[ni][nj] > 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1

def count_icebergs():
    visited = [[0] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and visited[i][j] == 0:
                bfs(i, j, visited)
                count += 1
    return count

# 빙산 녹이기
def melt_icebergs():
    melt = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                water_count = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
                        water_count += 1
                melt[i][j] = water_count
    
    for i in range(N):
        for j in range(M):
            graph[i][j] = max(0, graph[i][j] - melt[i][j])

years = 0
while True:
    count = count_icebergs()
    if count == 0:
        print(0)
        break
    if count >= 2:
        print(years)
        break
    melt_icebergs()
    years += 1
