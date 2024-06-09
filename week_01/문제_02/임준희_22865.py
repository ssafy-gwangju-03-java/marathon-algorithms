import sys
import heapq

def dijkstra(start, graph, n):
    # 모든 노드까지의 거리를 무한대로 초기화
    distance = [float('inf')] * (n + 1)
    # 시작 노드까지의 거리는 0으로 설정
    distance[start] = 0
    # 우선순위 큐 초기화
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    while priority_queue:
        # 현재 노드까지의 최단 거리와 노드 번호를 가져옴
        current_dist, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 노드면 무시
        if current_dist > distance[current_node]:
            continue
        
        # 인접 노드 탐색
        for adjacent, weight in graph[current_node]:
            # 인접 노드까지의 새로운 경로 거리 계산
            path_distance = current_dist + weight
            # 새로운 경로가 기존 경로보다 짧으면 최단 거리 갱신
            if path_distance < distance[adjacent]:
                distance[adjacent] = path_distance
                heapq.heappush(priority_queue, (path_distance, adjacent))
    return distance

input = sys.stdin.readline
n = int(input())
a, b, c = map(int, input().split())
m = int(input())

# 인접 리스트로 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 무한
INF = float('inf')
# 모든 노드에 대해 최단 거리가 가장 긴 값을 찾기 위해 초기화
min_distances = [INF] * (n + 1)

for start in (a, b, c):
    distances_from_start = dijkstra(start, graph, n)
    for i in range(1, n + 1):
        min_distances[i] = min(min_distances[i], distances_from_start[i])

# 최단 거리 중 가장 긴 값을 가지는 노드 찾기
farthest_node = 1
for i in range(2, n + 1):
    if min_distances[farthest_node] < min_distances[i]:
        farthest_node = i

print(farthest_node)