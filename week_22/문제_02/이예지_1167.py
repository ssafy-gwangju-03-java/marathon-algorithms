# 1167. 트리의 지름
import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    line = list(map(int, input().split()))
    node = line[0]
    for i in range(1, len(line) - 1, 2):
        graph[node].append((line[i], line[i + 1]))


def bfs(start):
    visited = [-1] * (V + 1)
    visited[start] = 0
    q = deque([(start, 0)])
    max_dist = 0
    max_node = start

    while q:
        now, dist = q.popleft()
        for next_node, weight in graph[now]:
            if visited[next_node] == -1:
                next_dist = dist + weight
                q.append((next_node, next_dist))
                visited[next_node] = next_dist
                if max_dist < next_dist:
                    max_dist = next_dist
                    max_node = next_node

    return max_node, max_dist


# 1번 노드에서 가장 먼 노드 찾기
far_node, _ = bfs(1)
# 그 노드에서 가장 먼 거리가 트리의 지름
_, diameter = bfs(far_node)

print(diameter)