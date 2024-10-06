import sys
import heapq

num_jewelry, num_buckets = map(int, sys.stdin.readline().split())
jewelry = [[*map(int, input().split())] for _ in range(num_jewelry)]
buckets = [int(input()) for _ in range(num_buckets)]

jewelry.sort()
buckets.sort()

total_value = 0
possible_jewelry = []

for bucket_capacity in buckets:
    # 가치가 높은 보석 순으로 우선순위 큐에 넣음
    while jewelry and jewelry[0][0] <= bucket_capacity:
        heapq.heappush(possible_jewelry, -jewelry[0][1])
        heapq.heappop(jewelry)

    # 가능한 보석 중 가장 높은 가치를 가진 보석을 선택
    if possible_jewelry:
        total_value -= heapq.heappop(possible_jewelry)

print(total_value)
