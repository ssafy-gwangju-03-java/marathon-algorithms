import sys
from collections import deque

gear_list = []

for _ in range(4):
    gear = deque(map(int, list(sys.stdin.readline()[:8])))
    gear_list.append(gear)

N = int(sys.stdin.readline())

# N번의 회전 커맨드 실행
for _ in range(N):
    target, rotate_dir = map(int, sys.stdin.readline().split())
    target -= 1

    # 각 톱니바퀴의 회전 방향을 기록할 list
    rotations = [0] * 4
    rotations[target] = rotate_dir

    # 현재 톱니바퀴의 왼쪽으로 탐색
    curr = target
    left = target - 1

    while left >= 0:
        if gear_list[left][2] != gear_list[curr][6]:
            rotations[left] = rotations[curr] * -1
        left -= 1
        curr -= 1

    # 현재 톱니바퀴의 오른쪽으로 탐색
    curr = target
    right = target + 1

    while right < 4:
        if gear_list[curr][2] != gear_list[right][6]:
            rotations[right] = rotations[curr] * -1
        right += 1
        curr += 1

    # 한번에 회전시켜주기
    for idx, direction in enumerate(rotations):
        gear_list[idx].rotate(direction)    # deque에 내장된 회전 함수, 양수면 오른쪽 음수면 왼쪽으로 회전시켜줌

print(sum(gear_list[i][0] * (2 ** i) for i in range(4)))