# https://www.acmicpc.net/problem/16947

## Referenced
# https://yjg-lab.tistory.com/429

import sys
from collections import deque

sys.setrecursionlimit(10**5)


def find_cycle(checked_nodes, level):
    """
    사이클 발생 확인 함수
    checked_nodes: 확인한 역 배열
    level: 깊이
    """
    for i in nodes[checked_nodes[-1]]:
        # 순환이 발생하기 위해선 최소 3개의 역이 필요 == 최소 깊이 3
        # 확인한 역 중에서 처음과 끝이 동일하고 3개 이상의 역이 연결되어 있다면 순환 확인
        if i == checked_nodes[0] and level >= 2:
            for j in checked_nodes:
                # 순환 내에 있는 역들은 순환선간의 거리가 0
                cycle[j] = 0
            return True

        if not visited[i]:
            # 현재 역 i를 방문처리 하고 사이클 확인
            visited[i] = 1
            if find_cycle(checked_nodes + [i], level + 1):
                return True
            # 현재 역 i는 사이클 관계가 아니므로 방문 취소 후 다음 역 확인
            visited[i] = 0
    return False


def get_distance():
    """
    각 역과 순환선 간의 거리 확인 함수
    """
    q = deque()
    # 순환선(사이클) 내에 있는 노드에서만 거리 측정을 위해 덱에 enque
    for i in range(1, N + 1):
        if cycle[i] == 0:
            q.append((i, 0))

    while q:
        now, dist = q.popleft()
        for to in nodes[now]:
            # 이전에 방문한 적 없는 노드라면 순환선과의 거리 설정 후
            # 덱에 enque
            if cycle[to] == -1:
                cycle[to] = dist + 1
                q.append((to, dist + 1))


input = sys.stdin.readline
N = int(input())
nodes = [[] for _ in range(N + 1)]

for _ in range(N):
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i)

cycle = [-1] * (N + 1)   # 순환선부터 각 역까지의 거리 저장 배열
visited = [0] * (N + 1)  # 사이클 확인을 위한 노드 방문 배열

for i in range(1, N + 1):
    visited[i] = 1
    if find_cycle([i], 0):  # 순환이 발견되면 break
        break
    visited[i] = 0

get_distance()
print(*cycle[1:])
