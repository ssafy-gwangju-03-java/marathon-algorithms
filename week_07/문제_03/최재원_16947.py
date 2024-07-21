import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline
N = int(input())

def dfs(node, depth):
    if visited[node]:
        # 현재 노드를 이미 방문했는데 사이클이 되는지 확인
        if depth - cycle_depth[node] >= 3:
            return node
        else:
            return -1

    # 방문한 노드 1
    visited[node] = 1
    cycle_depth[node] = depth

    for next_node in adjl[node]:
        cycle_start_node = dfs(next_node, depth + 1)

        if cycle_start_node != -1:
            # 순환선에 포함되면 2
            visited[node] = 2

            if node == cycle_start_node:
                return -1
            else:
                return cycle_start_node

    return -1

def bfs():
    queue = deque()

    for i in range(1, N + 1):
        if visited[i] == 2:
            queue.append(i)
            distances[i] = 0
        else:
            distances[i] = -1

    while queue:
        current_node = queue.popleft()
        for next_node in adjl[current_node]:
            if distances[next_node] == -1:
                queue.append(next_node)
                distances[next_node] = distances[current_node] + 1


adjl = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cycle_depth = [0] * (N + 1)
distances = [0] * (N + 1)

for _ in range(N):
    node1, node2 = map(int, input().split())
    adjl[node1].append(node2)
    adjl[node2].append(node1)

# 사이클 찾기
dfs(1, 0)

# 사이클로부터 거리 계산하기
bfs()

print(*distances[1:])
