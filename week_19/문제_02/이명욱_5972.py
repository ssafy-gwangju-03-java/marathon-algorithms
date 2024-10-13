import heapq


def dijkstra(s):
    q = []
    # 자기 자신과의 거리
    distance[s] = 0
    # (거리, 위치) 담기
    heapq.heappush(q, (0, s))
    while q:
        dist, cur = heapq.heappop(q)
        # 최솟값 보다 거리가 크다면 확인 x
        if distance[cur] < dist:
            continue
        # 이웃된 노드 확인
        for next in g[cur]:
            # 현재 노드까지의 거리 + 현재 노드에서 다음 노드까지의 거리
            cost = dist + next[1]
            # 최솟값 갱신
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance[N]


N, M = map(int, input().split())
inf = 1e9
distance = [inf]*(N+1)
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    # 양방향
    g[a].append((b,c))
    g[b].append((a,c))
print(dijkstra(1))
