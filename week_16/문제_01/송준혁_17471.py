# https://www.acmicpc.net/problem/17471

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
adjl = [[] for _ in range(N)]
not_connected = True
diff = sum(people)

for i in range(N):
    adjs = list(map(int, input().split()))
    for j in range(adjs[0]):
        adjl[i].append(adjs[j + 1] - 1)


# 개수가 N // 2개인 부분 집합 도출
def subset(idx, picks):
    global diff
    global not_connected

    if len(picks) == N // 2 or idx == N:
        # 선택된 선거구가 없는 경우 재귀 종료
        if not picks:
            return

        # BFS로 선거구 A와 선거구 B의 연결 확인
        not_picked = [i for i in range(N) if i not in picks]
        nodes_a, sum_a = bfs(picks)
        nodes_b, sum_b = bfs(not_picked)

        # 선거구 두 곳의 합이 N이면 두 선거구로 나뉠 수 있음
        if nodes_a + nodes_b == N:
            not_connected = False
            diff = min(diff, abs(sum_a - sum_b))
        return

    # 현재 선거구를 포함/미포함으로 나누어 재귀 진입
    subset(idx + 1, picks + [idx])
    subset(idx + 1, picks)


def bfs(picks):
    v = picks[0]
    q = deque()
    q.append(v)
    visited = [0] * N
    visited[v] = 1
    nodes = 1
    sums = people[v]

    while q:
        v = q.popleft()
        for adj in adjl[v]:
            if not visited[adj] and adj in picks:
                visited[adj] = 1
                q.append(adj)
                nodes += 1
                sums += people[adj]
    return nodes, sums


subset(0, [])
if not_connected:
    print(-1)
else:
    print(diff)
