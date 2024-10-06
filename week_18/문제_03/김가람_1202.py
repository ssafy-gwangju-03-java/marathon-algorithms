import sys, heapq

N, K = map(int, sys.stdin.readline().split())
jewelry = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
jewelry.sort()
bags.sort()

ans = 0

# 각 가방별로 보석 가치의 최댓값을 산출하기 위해 사용
temp = []

for bag in bags:

    # 현재 가방에 담을 수 있는 보석 중 가장 무거운 보석을 뽑을 때 까지 heappop
    # temp에는 현재 가방에 담을 수 있는 보석들의 가격을 오름차순으로 담아줌
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewelry)[1])

    # 가장 비싼 보석의 가격을 더해주기
    if temp:
        ans += -1 * heapq.heappop(temp)

print(ans)