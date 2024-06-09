import heapq

INF = 100000


# s: 시작지점
def dijkstra(s):
    # 시작지점에서부터 최단거리
    dist = [INF] * (N + 1)
    dist[s] = 0  # 자기자신까지 거리는 0
    queue = []

    heapq.heappush(queue, (0, s))  # (거리, 노드) 형태로 큐에 삽입
    while queue:
        d, c = heapq.heappop(queue)
        if dist[c] < d:  # 이미 처리된 애는 패스
            continue
        # 현재 노드와 연결된 노드들에 대해 탐색
        for n, nd in graph[c]:
            total_dist = d + nd  # 현재까지의 거리 + 다음 간선 거리
            if total_dist < dist[n]:  # 새로 계산한 거리가 기존보다 짧으면 갱신
                dist[n] = total_dist
                heapq.heappush(queue, (total_dist, n))  # 갱신된 (거리, 노드)를 큐에 추가
    return dist


# 자취할 땅 후보 개수 N
N = int(input())
# 친구 A,B,C 위치 (같을수있음)
# friends = list(map(int, input().split()))
A, B, C = map(int, input().split())
# 도로 개수 M
M = int(input())
# 땅1, 땅2, 도로길이(양방향)
# roads = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)] # 초기화를 잘못해서 틀렸다..
for _ in range(M):
    # 땅1, 땅2, 도로길이(양방향)
    D, E, road = map(int, input().split())
    # 무향그래프
    graph[D].append([E, road])
    graph[E].append([D, road])

# 친구들 최단거리
dist_A = dijkstra(A)
dist_B = dijkstra(B)
dist_C = dijkstra(C)

max_dist = 0
ans = 0
for i in range(1, N + 1):
    # 친구들로부터 최단거리 중 가장 작은값이랑 비교해서 최대거리 갱신
    if max_dist < min(dist_A[i], dist_B[i], dist_C[i]):
        max_dist = min(dist_A[i], dist_B[i], dist_C[i])
        ans = i
print(ans)
