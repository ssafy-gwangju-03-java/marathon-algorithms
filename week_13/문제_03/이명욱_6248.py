import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(now, lst, visited):
    if visited[now]:
        return
    visited[now] = 1
    for next in lst[now]:
        dfs(next, lst, visited)

# 인접리스트
adl = [[] for _ in range(n + 1)]
rev_adl = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adl[a].append(b)
    rev_adl[b].append(a)

S, T = map(int, input().split())

# S -> T
startS = [0] * (n + 1)
startS[T] = 1
dfs(S, adl, startS)

# T -> S
startT = [0] * (n + 1)
startT[S] = 1
dfs(T, adl, startT)

# (출근길 경로에 S는 여러 번 등장해도 되고, 퇴근길 경로에 T는 여러 번 등장해도 된다.)
# 위 조건으로 역방향 케이스도 구해야 함.

# x -> S
endS = [0] * (n + 1)
dfs(S, rev_adl, endS)

# x -> T
endT = [0] * (n + 1)
dfs(T, rev_adl, endT)

cnt = 0
for i in range(1, n + 1):
    if startS[i] and startT[i] and endS[i] and endT[i]:
        cnt += 1

# 출발, 도착 점 빼기
print(cnt - 2)