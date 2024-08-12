# 14698 전생했더니 슬라임 연구자였던 건에 대하여(Hard)
# 작은거 두개 뽑아서 곱하고 다시 넣음 -> 이걸 끝까지 반복 : 누적해서 계속 곱해지므로 작은 숫자가 여러번 곱해지는게 최소값이 나오므로
import sys
import heapq

input = sys.stdin.readline  # 이거 처리 안해주면 시간초과
t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    heap = []
    for i in lst:
        heapq.heappush(heap, i)
    ans = 1
    while len(heap) >= 2:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        heapq.heappush(heap, x * y)
        ans *= x * y
    print(ans % 1000000007)
