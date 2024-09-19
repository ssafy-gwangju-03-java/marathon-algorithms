# 17471 게리맨더링
from itertools import combinations
from collections import deque

n = int(input())
lst = list(map(int, input().split()))
ans = 1001
line = [[] for _ in range(n + 1)]

for i in range(n):
    link = list(map(int, input().split()))
    for j in range(1, link[0] + 1):
        line[i].append(link[j] - 1)


def bfs(case): 
    first = case[0]
    q = deque()
    q.append(first)
    vis = [first]
    cnt = 0
    while q:
        now = q.popleft()
        cnt += lst[now]
        for next in line[now]:
            if next not in vis and next in case:
                q.append(next)
                vis.append(next)
    return cnt, len(vis)


# 모든 케이스 탐색
for i in range(1, n // 2 + 1):
    for case in combinations(range(n), i): # 모든 케이스를 다 뽑아서 확인
        sum1, a = bfs(case)
        sum2, b = bfs([x for x in range(n) if x not in case])
        if a + b == n: # 두 케이스 다 연결되어있는경우
            ans = min(ans, abs(sum1 - sum2))
if ans == 1001:
    print(-1)
else:
    print(ans)
