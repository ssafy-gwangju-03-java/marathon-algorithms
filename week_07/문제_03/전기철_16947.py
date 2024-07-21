import sys
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())

lst = [[] for _ in range(n + 1)]
for _ in range(n):  # 양방향 연결
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

# 일단 순환선을 찾아야함

circle = [3001] * (n + 1)  # 거리
vis = [0] * (n + 1)
chk = 0


def dfs(d, cnt):  # 순환선 찾기
    global chk
    if chk:
        return
    for i in lst[d[-1]]:  # 뒤로 붙이면서 순환선 완성되나 확인
        if i == d[0] and cnt >= 3:
            # 처음으로 돌아옴(완성) / 순환선이 만들어지려면 3개이상은 있어야함
            for j in d:
                circle[j] = 0
            chk = 1
            return
        if not vis[i]:
            vis[i] = 1
            dfs(d + [i], cnt + 1)
            vis[i] = 0


def bfs():
    q = deque()
    for i in range(1, n + 1):
        if circle[i] == 0:  # 순환선 내부 점이면
            q.append((i, 0))  # 점과 거리 넣기
    while q:
        now, dist = q.popleft()
        for i in lst[now]:
            if circle[i] == 3001:  # 순환선 아닌거면
                circle[i] = dist + 1
                q.append((i, dist + 1))


for i in range(1, n + 1):
    vis[i] = 1
    dfs([i], 1)
    vis[i] = 0

bfs()

print(*circle[1:])
