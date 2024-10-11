import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

adjl = [[] for _ in range(V + 1)]

for _ in range(E):
    p, q, r = map(int, sys.stdin.readline().split())
    adjl[p].append((q, r))
    adjl[q].append((p, r))

# 시간복잡도를 고려하여 우선순위 큐를 사용한 다익스트라
def djk():
    dist = [1e9] * (V + 1)
    q = []

    dist[1] = 0
    q.append((0, 1))

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        for next_node, next_dist in adjl[curr_node]:
            if curr_dist + next_dist < dist[next_node]:
                new_dist = curr_dist + next_dist
                dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    return dist[V]

print(djk())
