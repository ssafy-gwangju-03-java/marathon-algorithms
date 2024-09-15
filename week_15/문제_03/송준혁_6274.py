# https://softeer.ai/practice/6274

## Referenced
# https://talktato.tistory.com/31

import sys
from collections import deque

input = sys.stdin.readline

N, T = map(int, sys.stdin.readline().split())
check = [[0] * N for _ in range(N)]

d = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
signal = {
    # 현재 시각, 교차로 위치 신호 정보: (직전 위치, [교차로의 신호별 방향 배열])
    1: (d["right"], [d["up"], d["right"], d["down"]]),
    2: (d["up"], [d["left"], d["up"], d["right"]]),
    3: (d["left"], [d["up"], d["left"], d["down"]]),
    4: (d["down"], [d["right"], d["down"], d["left"]]),
    5: (d["right"], [d["up"], d["right"]]),
    6: (d["up"], [d["left"], d["up"]]),
    7: (d["left"], [d["left"], d["down"]]),
    8: (d["down"], [d["down"], d["right"]]),
    9: (d["right"], [d["right"], d["down"]]),
    10: (d["up"], [d["up"], d["right"]]),
    11: (d["left"], [d["up"], d["left"]]),
    12: (d["down"], [d["left"], d["down"]]),
}

signals = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        signals[i][j].extend(list(map(int, input().split())))


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def pathfinder():
    result = set()
    q = deque()
    # 현재 위치, 직전 방향, 현재 시각
    q.append(((0, 0), (-1, 0), 0))

    while q:
        curr_pos, prev_direction, curr_time = q.popleft()
        # 방문 교차로 저장
        result.add((curr_pos[0], curr_pos[1]))
        # 현재 교차로 신호 = 현재 시각의 현재 위치의 signals 배열 원소
        curr_signal = signals[curr_pos[0]][curr_pos[1]][curr_time % 4]
        # 현재 신호의 방향
        direction = signal[curr_signal]

        # 직전 위치와 현재 신호의 진행 방향이 같다면
        if prev_direction == direction[0]:
            # 모든 신호의 진행 방향을 덱에 저장 후 시간 증가시킴
            for dr, dc in direction[1]:
                nr, nc = curr_pos[0] + dr, curr_pos[1] + dc
                if is_valid(nr, nc) and curr_time < T:
                    q.append(((nr, nc), (dr, dc), curr_time + 1))

    return len(result)


print(pathfinder())
