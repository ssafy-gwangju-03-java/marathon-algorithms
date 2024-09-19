from collections import deque

def bfs(start, g, v):
    q = deque()
    q.append(start)
    v[start] = 1
    while q:
        now = q.popleft()
        for go in g[now]:
            if v[go]:
                continue
            v[go] = 1
            q.append(go)

# 노드 수, 간선 수
n, m = map(int, input().split())

# 그래프와 역방향 그래프 초기화
graph = [[] for _ in range(n+1)]
graph_re = [[] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_re[b].append(a)

# 시작점 도착점
S, T = map(int, input().split())

# S에서 출발하는 BFS
fromS = [0] * (n+1)
fromS[T] = 1          # S->T 1로 미리 세팅
bfs(S, graph, fromS)

# T에서 출발하는 BFS
fromT = [0] * (n+1)
fromT[S] = 1          # T->S 1로 미리 세팅
bfs(T, graph, fromT)

# S로 도착하는 BFS (역방향)
toS = [0] * (n+1)
bfs(S, graph_re, toS)

# T로 도착하는 BFS (역방향)
toT = [0] * (n+1)
bfs(T, graph_re, toT)

answer = 0

# 모든 노드에 대해 검사
for i in range(1, n+1):
    # 시작점과 도착점 제외
    if i == S or i == T:
        continue
    # 모든 조건을 만족하는 노드 카운트
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        answer += 1

print(answer)
# https://door-of-tabris.tistory.com/entry/Softeer-6%EC%B0%A8%EA%B8%B0%EC%B6%9C-%EC%B6%9C%ED%87%B4%EA%B7%BC%EA%B8%B8python#google_vignette