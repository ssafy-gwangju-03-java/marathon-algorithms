# 출퇴근길

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

nodes = [[] for _ in range(n + 1)]
reverse_nodes = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    nodes[x].append(y)
    reverse_nodes[y].append(x)

S, T = map(int, input().split())

def dfs(now, graph, visited):
    if visited[now] == 1:
        return

    else:
        visited[now] = 1
        for node in graph[now]:
            dfs(node, graph, visited)

    return

start_S = [0] * (n + 1)
start_S[T] = 1
dfs(S, nodes, start_S)

start_T = [0] * (n + 1)
start_T[S] = 1
dfs(T, nodes, start_T)

end_S = [0] * (n + 1)
dfs(S, reverse_nodes, end_S)

end_T = [0] * (n + 1)
dfs(T, reverse_nodes, end_T)

result = 0
for i in range(1, n + 1):
    if start_S[i] and start_T[i] and end_S[i] and end_T[i]:
        result += 1

print(result - 2)