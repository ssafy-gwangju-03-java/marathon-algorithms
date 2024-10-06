# 1202 보석 도둑
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
maxWeights = [int(input()) for _ in range(k)]
# 정렬 -->  고려할 범위 줄이기
info.sort()
maxWeights.sort()

ans = 0
temp = []   # max 저장하려고
i = 0

for mw in maxWeights:
    while i < n and info[i][0] <= mw:
        heapq.heappush(temp, -info[i][1])   # info 속 음수를 힙에 저장(heapq가 최소힙이니까 -)
        i += 1

    if temp:
        ans -= heapq.heappop(temp)  # 음수로 저장해놓은 거 빼기

print(ans)
