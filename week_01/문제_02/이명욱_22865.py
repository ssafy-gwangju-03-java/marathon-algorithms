# 가장 먼 곳
# 참고 : 이코테 7. 최단 경로 알고리즘 https://www.youtube.com/watch?v=acqm9mM1P6o

import heapq, sys
input = sys.stdin.readline

INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    # 힙큐에 거리, 시작 노드 삽입
    heapq.heappush(q, (0, start))
    # 시작하는 노드는 당연히 거리가 0
    distance[start] = 0

    # 큐가 빌 때까지
    while q:
        # 최단 거리가 가장 짤은 노드 꺼내기
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드라면 넘어가기
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                # 최단 거리 갱신 및 힙큐 삽입
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # 최단 거리 리스트 반환
    return distance
#     min_v = min(distance[A], distance[B], distance[C])
#     return min_v

# 1부터 N까지의 땅 후보의 개수
N = int(input())
# 친구들이 사는 위치
A, B, C = map(int, input().split())
# 도로의 개수
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))

# 각 정점에서 A, B, C로의 거리 구하기
dist_from_a = dijkstra(A)
dist_from_b = dijkstra(B)
dist_from_c = dijkstra(C)

# 가장 가까운 친구집 중 제일 먼 곳 확인
max_d = -1
# 가장 가까운 친구집 중 제일 먼 곳일때의 내 집 위치
result = 0

# 1부터 N까지 위치일 때 친구들 집까지의 거리 확인
for j in range(1, N + 1):
    # 친구집 위치일땐 할 필요 x
    if j == A or j == B or j == C:
        continue

    # A, B, C에서 j로 가는 거리 중 가장 작은 값
    min_d = min(dist_from_a[j], dist_from_b[j], dist_from_c[j])

    # 친구들이 살고 있는 집으로부터 가장 먼 곳 일때
    if max_d < min_d:
        # 거리, 내 집 갱신
        # 가장 먼 곳이 여러 곳일때 번호가 가장 작은 땅의 번호->오름차순으로 확인하니까 신경 안써도 됨
        max_d = min_d
        result = j

print(result)


# 시간 초과 -> 모든 정점에서 시작해서 친구들 집 및 나머지 집들의 최단 거리를 구함(애는 다익 N-3 번 하게 됨)
# => 친구들 집에서 시작해서 최단 거리 구해놓으면 다익스트라 3번만 하면 됨

# max_d = -1
# result = 0
#
# for j in range(1, N + 1):
#     if j == A or j == B or j == C:
#         continue
#     min_d = dijkstra(j)
#     if max_d > min_d:
#         continue
#     if max_d < min_d:
#         max_d = min_d
#         result = j
#     elif max_d == min_d:
#         result = min(result, j)
#
# print(result)