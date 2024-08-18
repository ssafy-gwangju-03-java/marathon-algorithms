import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    slime = list(map(int, sys.stdin.readline().split()))

    # 가장 작은 슬라임부터 차례대로 곱해준다
    heapq.heapify(slime)
    answer = 1

    while len(slime) > 1:
        a, b = heapq.heappop(slime), heapq.heappop(slime)
        answer *= a * b

        # 곱해준 슬라임이 힙 안에서 또 다시 정렬되어야 최솟값이 보장된다
        heapq.heappush(slime, a * b)

    print(int(answer % 1_000_000_007))

