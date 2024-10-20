# https://www.acmicpc.net/problem/13549

## Referenced
# https://velog.io/@silver_star/백준-13549-숨바꼭질-3-다익스트라-BFS

import sys
from collections import deque


def is_valid(pos):
    return 0 <= pos <= 100000


def finder(N, K):
    q = deque()
    q.append((N, 0))

    # 해당 위치에 도달하는 시간을 저장할 방문 배열
    # 0 -> 100000 이동 최대 시간인 100000으로 초기화
    visited = [100000] * 100001
    visited[N] = 0

    while q:
        # 덱에 들어있는 튜플을 순회하며 세 가지 이동 방법 탐색
        # 이전에 방문했을 때의 시간이 현재 방문 시간보다 길 경우 방문 배열 새로 고침
        current, count = q.popleft()

        target = current + 1
        if is_valid(target) and visited[target] > count + 1:
            visited[target] = count + 1
            q.append((target, visited[target]))

        target = current - 1
        if is_valid(target) and visited[target] > count + 1:
            visited[target] = count + 1
            q.append((target, visited[target]))

        if current != 0:
            target = current * 2
            if is_valid(target) and visited[target] > count:
                visited[target] = count
                q.append((target, visited[target]))

    return visited[K]


input = sys.stdin.readline
N, K = map(int, input().split())
print(finder(N, K))
