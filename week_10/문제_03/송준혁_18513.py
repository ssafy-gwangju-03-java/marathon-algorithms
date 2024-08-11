# https://www.acmicpc.net/problem/18513

## Referenced
# https://velog.io/@juuiccyy/백준-18513-샘터-Python

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
springs = list(map(int, input().split()))


def builder():
    q = deque()
    # 샘터, 집의 위치와 집의 불행도를 저장할 딕셔너리
    grid = {}
    count, unhappiness = 0, 0

    for spring in springs:
        q.append(spring)
        grid[spring] = 0

    while q:
        start = q.popleft()
        for i in range(-1, 2, 2):
            target = start + i

            # 목표 위치에 지어진 집이 없을 경우
            if target not in grid.keys():
                # 목표 위치에 지은 집의 불행도는 시작 위치 + 1
                grid[target] = grid[start] + 1
                # 집 개수 ++, 새로운 집의 불행도 추가
                count += 1
                unhappiness += grid[target]

                if count >= K:
                    return unhappiness
                q.append(target)


print(builder())
