# 서울 지하철 2호선

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(500*500)

N = int(input())

line = [[] for _ in range(N + 1)]

for i in range(N):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)

visited = [0] * (N + 1)
stack = []
cycle = []

def dfs(v, parent):
    visited[v] = 1
    stack.append(v)

    for neighbor in line[v]:
        if visited[neighbor] == 0:
            if dfs(neighbor, v):
                return True
        elif neighbor != parent:
            cycle_start_index = stack.index(neighbor)
            global cycle
            cycle = stack[cycle_start_index:]
            return True

    stack.pop()
    return False

def bfs():
    distances = [-1] * (N + 1)
    q = deque()

    for node in cycle:
        q.append(node)
        distances[node] = 0

    while q:
        current = q.popleft()
        for neighbor in line[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                q.append(neighbor)

    return distances

# dfs를 1번 역에서 시작
dfs(1, -1)

# bfs로 거리 계산
distances = bfs()

print(' '.join(map(str, distances[1:])))
