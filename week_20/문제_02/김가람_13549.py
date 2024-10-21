import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        curr = q.popleft()

        if curr == K:
            return line[curr]

        # 순간이동
        if curr and curr * 2 <= 100_000:
            next = curr * 2
            visited[next] = True
            line[next] = line[curr]
            q.append(next)

        # 걷기
        for i in (-1, 1):
            next = curr + i
            if 0 <= next <= 100_000 and not visited[next]:
                visited[next] = True
                line[next] = line[curr] + 1
                q.append(next)

line = [0] * 100_001
visited = [False] * 100_001

print(bfs(N, visited))



