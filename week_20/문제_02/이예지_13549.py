# 13549 숨바꼭질 3
import heapq
import sys
input = sys.stdin.readline

def solve(s, e):
    distance = [float('inf')] * 100001
    distance[s] = 0
    Q = [(0, s)]

    while Q:
        time, pos = heapq.heappop(Q)
        if pos == e:
            return time
        if time > distance[pos]:
            continue

        # 순간이동
        if pos*2 <= 100000 and time < distance[pos*2]:
            distance[pos*2] = time
            heapq.heappush(Q, (time, pos*2))

        # 걷기
        # 왼쪽
        if pos > 0 and time+1 < distance[pos-1]:
            distance[pos-1] = time+1
            heapq.heappush(Q, (time+1, pos-1))

        # 오른쪽
        if pos < 100000 and time+1 < distance[pos+1]:
            distance[pos+1] = time+1
            heapq.heappush(Q, (time+1, pos+1))

n, k = map(int, input().split())
print(solve(n, k))