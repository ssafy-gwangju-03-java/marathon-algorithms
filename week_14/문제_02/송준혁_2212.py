# https://www.acmicpc.net/problem/2212

## Referenced
# https://velog.io/@jkh9615/알고리즘-백준-11000-강의실-배정-Java-wskzqzk6

import sys

input = sys.stdin.readline


def station(N, K, sensors):
    """
    1. 센서 좌표 오름차순 정렬
    2. 각 센서간 거리 차이 계산 후 내림차순 정렬
    3. 집중국이 K개라면 각 집중국 간 사이는 K - 1개
       -> 센서 간 거리 차이 배열에서 큰 순서대로 K - 1개 무시 가능 
       -> 센서 간 거리 차이 배열에서 K - 1번 인덱스부터의 합
    """

    # 집중국이 센서 개수보다 크거나 같으면 개당 한개씩 배치
    if K >= N:
        return 0

    sensors.sort()

    diff = []
    for i in range(N - 1):
        diff.append(sensors[i + 1] - sensors[i])
    diff.sort(reverse=True)

    sum_diff = sum(diff[K - 1 :])
    return sum_diff


N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

print(station(N, K, sensors))
