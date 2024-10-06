import sys
import heapq

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

# 무게가 가벼운 순으로 정렬
jewelry = sorted([list(map(int, input().split())) for _ in range(N)])
# 가방 용량이 작은 순으로 정렬
bags = sorted([int(input()) for _ in range(K)])

# 가격 기준 최대 힙 큐
pq = []
answer = 0
# 가방 용량이 작은 순서대로 진행
for bag in bags:
    # 보석의 무게가 가방의 무게보다 가벼운걸 우선순위큐에 넣기
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(pq, -jewelry[0][1])
        heapq.heappop(jewelry)

    # 들어갈 수 있는 보석이 있으면
    if pq:
        # 가장 비싼 보석 넣기
        answer += heapq.heappop(pq)
    # 보석이 더이상 없으면 종료
    elif not jewelry:
        break

print(-answer)
