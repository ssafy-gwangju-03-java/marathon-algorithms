import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# 순환선 찾기 
def find_cycle():
    visited = [False] * (N+1) 
    parent = [0] * (N+1)  
    cycle = [] 

    def dfs(node, prev):
        visited[node] = True
        for next_node in graph[node]:
            if next_node == prev:  # 직전 방문 노드는 건너뛰기
                continue
            if visited[next_node]:  
                curr = node
                while curr != next_node:
                    cycle.append(curr)
                    curr = parent[curr]
                cycle.append(next_node)
                return True
            parent[next_node] = node
            if dfs(next_node, node): 
                return True
        return False

    dfs(1, 0) 
    return cycle

cycle = set(find_cycle())

# B각 역과 순환선 사이의 거리 계산 
def bfs():
    distance = [0] * (N+1)  # 각 역의 순환선까지의 거리 저장
    queue = deque(cycle)  # 순환선 역들로 큐 초기화
    visited = set(cycle)  # 방문한 역 체크

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                distance[next_node] = distance[node] + 1 
                visited.add(next_node)
                queue.append(next_node)

    return distance


distances = bfs()
print(*distances[1:])