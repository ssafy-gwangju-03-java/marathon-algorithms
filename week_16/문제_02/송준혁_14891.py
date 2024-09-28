# https://www.acmicpc.net/problem/14891

## Referenced
# https://velog.io/@khc41/백준-14891번-톱니바퀴-C-삼성-기출-amdofa1x

import sys

input = sys.stdin.readline


def check_left(idx, direction):
    """
    - 현 위치 톱니바퀴의 9시 톱니와 그 왼쪽의 톱니바퀴의 3시 톱니 비교
    - 다른 극이라면 현재 톱니바퀴의 회전 방향과 반대 방향으로 회전시킨 후,
      현 위치의 왼쪽 톱니바퀴로 이동 후 반복
    """
    if idx <= 0:
        return
    if gears[idx][6] != gears[idx - 1][2]:
        to_rotate[idx - 1] = direction * -1
        check_left(idx - 1, direction * -1)


def check_right(idx, direction):
    """
    - 현 위치 톱니바퀴의 3시 톱니와 그 오른쪽의 톱니바퀴의 9시 톱니 비교
    - 다른 극이라면 현재 톱니바퀴의 회전 방향과 반대 방향으로 회전시킨 후,
      현 위치의 오른쪽 톱니바퀴로 이동 후 반복
    """
    if idx >= 3:
        return
    if gears[idx][2] != gears[idx + 1][6]:
        to_rotate[idx + 1] = direction * -1
        check_right(idx + 1, direction * -1)


gears = [input().rstrip() for _ in range(4)]
K = int(input())

for _ in range(K):
    c, r = map(int, input().split())

    # 톱니바퀴별 회전 유무/방향을 저장할 배열
    # 매 명령 입력시마다 초기화
    to_rotate = [0] * 4

    to_rotate[c - 1] = r
    check_left(c - 1, r)
    check_right(c - 1, r)

    for i in range(4):
        # 오른쪽 회전이면 마지막 자리가 처음으로 이동
        if to_rotate[i] == 1:
            gears[i] = gears[i][7:] + gears[i][:7]
        # 왼쪽 회전이면 첫 번째 자리가 마지막으로 이동
        elif to_rotate[i] == -1:
            gears[i] = gears[i][1:] + gears[i][0]

result, multiplier = 0, 1
for i in range(4):
    result += int(gears[i][0]) * multiplier
    multiplier *= 2

print(result)
