import sys, heapq
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    N = int(input())
    slime = list(map(int, input().split()))

    electricity = 1

    hq = []

    for s in slime:
        heapq.heappush(hq, s)

    while len(hq) >= 2:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        big_slime = a * b
        electricity *= big_slime
        electricity %= 1_000_000_007
        heapq.heappush(hq, big_slime)

    print(electricity)
