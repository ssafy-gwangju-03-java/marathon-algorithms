import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)


# 순환선을 찾아낼 DFS 함수
# curr == 현재 탐색중인 역
# order == DFS의 방문 순서
# visited == [N - 1번째 역의 order]
def dfs(curr, order, visited):

    # 이미 순환선을 찾았다면 return
    if loop:
        return

    # 방문했던 곳으로 다시 돌아왔다 == 순환선
    if visited[curr]:

        # 해당 역의 순서가 순환선의 시작 순서보다 크거나 같다
        # == 순환선의 시작 이후에 방문했다
        # == 순환선에 포함된다
        for i in range(N):
            if visited[i] >= visited[curr]:
                loop.append(i)
        return


    visited[curr] = order

    # 인접 리스트에서 이미 방문했던 정점들을 지워줘야 되돌아가지 않을 수 있다
    for i in range(N):
        if i in adjl[curr]:
            adjl[curr].remove(i)
            adjl[i].remove(curr)
            dfs(i, order + 1, visited)
            adjl[curr].append(i)
            adjl[i].append(curr)

    visited[curr] = 0


# 순환선인 역들로부터의 거리를 측정해 줄 BFS 함수
def bfs():

    # 시작 정점은 순환선에 해당되는 역들
    visited = [False] * N
    for vertex in loop:
        visited[vertex] = True
    q = deque(loop)

    # 순환선으로부터의 거리
    dist = 0

    while q:
        q_size = len(q)

        for _ in range(q_size):
            curr = q.popleft()
            answer[curr] = dist

            for next in adjl[curr]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)

        dist += 1


N = int(sys.stdin.readline())
adjl = [[] for _ in range(N)]

for _ in range(N):
    p, q = map(int, sys.stdin.readline().split())
    adjl[p - 1].append(q - 1)
    adjl[q - 1].append(p - 1)

loop = []
dfs(0, 1, [0] * N)

answer = [0] * N
bfs()
print(*answer)




# 시간초과 코드
# -> 역마다 dfs 돌려서 약 N * N * N
#
# def dfs(s, curr, order, dist):
#     if answer[s]:
#         return
#
#     if dist[curr]:
#         answer[s] = dist[curr] - 1
#         return
#
#     dist[curr] = order
#
#     for i in range(N):
#         if i in adjl[curr]:
#             adjl[curr].remove(i)
#             adjl[i].remove(curr)
#             dfs(s, i, order + 1, dist)
#             adjl[curr].append(i)
#             adjl[i].append(curr)
#
#     dist[curr] = 0
#
#
# N = int(sys.stdin.readline())
# adjl = [[] for _ in range(N)]
#
# for _ in range(N):
#     p, q = map(int, sys.stdin.readline().split())
#     adjl[p - 1].append(q - 1)
#     adjl[q - 1].append(p - 1)
#
# answer = [0] * N
#
# for i in range(N):
#     dfs(i, i, 1, [0] * N)
#
# print(*answer)
