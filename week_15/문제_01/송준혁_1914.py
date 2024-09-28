# https://www.acmicpc.net/problem/1914

## Referenced
# https://namu.wiki/w/하노이의 탑
# https://velog.io/@miiingirok/백준-1914.-하노이탑-Python

import sys

input = sys.stdin.readline

N = int(input())


def hanoi(N, pole_init, pole_target, pole_thru):

    # 가장 위에 있는 원판을 목표 장대로 옮김
    if N == 1:
        # moves.append((pole_init, pole_target))
        print(pole_init, pole_target)
    else:
        # N 원판을 목표 장대로 옮기기 위해선 N - 1까지의 원판을
        # 목표 장대를 통해 보조 장대로 옮겨야 함
        hanoi(N - 1, pole_init, pole_thru, pole_target)

        # N - 1까지의 원판이 보조 장대로 이동했으므로, N 원판을 목표 장대로 옮김
        # moves.append((pole_init, pole_target))
        print(pole_init, pole_target)

        # 목표 장대에 도착한 N 원판을 제외한 나머지 원판을
        # 현재 위치한 보조 장대에서 시작 장대를 통해 목표 장대로 이동
        hanoi(N - 1, pole_thru, pole_target, pole_init)

# 하노이탑 이동 횟수
print(2**N - 1)

if N <= 20:
    hanoi(N, 1, 3, 2)
