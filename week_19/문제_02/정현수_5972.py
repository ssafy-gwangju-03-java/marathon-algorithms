import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start):
    dist = [21e8] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_cost > dist[current_node]:
            continue

        for next_cost, next_node in graph[current_node]:
            total_cost = current_cost + next_cost

            # 더 적은 비용으로 도달할 수 있다면 갱신
            if total_cost < dist[next_node]:
                dist[next_node] = total_cost
                heapq.heappush(pq, (total_cost, next_node))
    return dist

result = dijkstra(0)
print(result[n - 1]) 