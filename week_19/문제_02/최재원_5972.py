import sys, heapq

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append((b, c))
    adjl[b].append((a, c))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adjl[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e9)
distance = [INF] * (N + 1)
dijkstra()

print(distance[-1])
