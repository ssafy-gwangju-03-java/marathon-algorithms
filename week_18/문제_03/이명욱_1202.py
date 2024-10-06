import heapq

N, K = map(int, input().split())
# 보석
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, input().split())))
# 가방
bags = []
for _ in range(K):
    bags.append(int(input()))
# 오름차순 정렬
bags.sort()

answer = 0
tmp_jew = []

# 각 가방에 담을 수 있는 모든 보석은 최소힙
# 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석을 찾을 땐 최대힙
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break

print(answer)