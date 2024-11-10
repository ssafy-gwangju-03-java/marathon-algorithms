# https://www.acmicpc.net/problem/1011

## Referened
# https://st-lab.tistory.com/79

import sys
from math import sqrt

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    count = 0

    # 총 이동 거리
    distance = Y - X

    # 특정 거리에서의 최대 이동 값 = 거리의 소수점을 제외한 제곱근
    max_v = int(sqrt(distance))

    # 거리가 완전제곱수일 경우
    if distance == max_v**2:
        count = 2 * max_v - 1
    # 거리가 다음 max_v 값보다 작을 경우
    elif distance <= max_v**2 + max_v:
        count = 2 * max_v
    # 거리가 더 클 경우
    else:
        count = 2 * max_v + 1

    print(count)
