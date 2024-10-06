# 1202 보석도둑

import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

bag.sort()
lst.sort()
ans = 0
use = []
for i in bag:
    while lst and lst[0][0] <= i:
        heapq.heappush(use, -lst[0][1]) # heapq가 최소힙이므로 음수로 넣어서 최대힙으로 변경
        heapq.heappop(lst)
    if use:
        ans -= heapq.heappop(use) # 제일 큰 가중치값(-)을 꺼내서 갱신해줌
print(ans)
