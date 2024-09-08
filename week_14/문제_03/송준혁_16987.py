# https://www.acmicpc.net/problem/16987

## Referenced
# https://velog.io/@yoonuk/백준-16987-계란으로-계란치기-Java자바

import sys

input = sys.stdin.readline


def breaker(idx, count):
    global result, eggs

    # 최근에 든 계란이 마지막 계란일 경우 종료
    if idx == N:
        result = max(result, count)
        return

    # 현재 계란 내구도가 없거나 모든 계란이 깨져있다면 다음으로 넘어감
    if eggs[idx][0] <= 0 or count == N - 1:
        breaker(idx + 1, count)
        return

    for target in range(N):
        # 자기 자신과 내구도 없는 계란 무시
        if target == idx or eggs[target][0] <= 0:
            continue

        # 손에 든 계란과 다른 계란의 내구도 감소
        eggs[target][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[target][1]

        # 깨진 계란 개수 세기
        breaks = 0
        if eggs[idx][0] <= 0:
            breaks += 1
        if eggs[target][0] <= 0:
            breaks += 1

        # 다음 계란으로 넘어감
        breaker(idx + 1, count + breaks)

        # 계란 복구
        eggs[target][0] += eggs[idx][1]
        eggs[idx][0] += eggs[target][1]


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
result = 0

breaker(0, 0)
print(result)
