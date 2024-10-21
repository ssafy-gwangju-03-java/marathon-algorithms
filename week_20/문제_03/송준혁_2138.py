# https://www.acmicpc.net/problem/2138

## Referenced
# https://staticvoidlife.tistory.com/143
# https://burningjeong.tistory.com/409
# https://velog.io/@cjkangme/백준-2138.-전구와-스위치-파이썬

import sys


def bulb_switcher(i, lights):
    """
    입력된 인덱스 기준으로 전구를 켜고 끔
    """
    if i != 0:
        lights[i - 1] = 1 if lights[i - 1] == 0 else 0
    lights[i] = 1 if lights[i] == 0 else 0
    if i != N - 1:
        lights[i + 1] = 1 if lights[i + 1] == 0 else 0
    return lights


def greedy(count, lights):
    """
    - i번 전구에 영향을 주는건 (i + 1)번째 전구
    - 따라서 i번 전구의 상태가 목표와 다르다면, (i + 1)번째 스위치를 눌러야 함
    - 스위치를 누르기 시작하는 위치가 중요, 스위치를 누르는 순서는 중요하지 않음
    - 0번 스위치는 그리디 탐색 이전에 눌림 여부가 결정되어 있기 때문에,
      1부터 N - 1까지 순회하며 해당 위치에서 스위치를 눌러봄
    - 최종 순회 결과가 목표 전구 상태와 같은 상태면 가능하므로 count 반환
    """
    for i in range(1, N):
        if lights[i - 1] != target[i - 1]:
            lights = switch_on(i, lights)
            count += 1
    return count, lights


input = sys.stdin.readline
N = int(input())
lights = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))
lights_backup = [i for i in lights]

# 0번 스위치를 누르지 않고 그리디 탐색
result_1, lights = greedy(0, lights)
if lights != target:
    result_1 = -1

# 0번 스위치를 누른 후 그리디 탐색
lights = switch_on(0, lights_backup)
result_2, lights = greedy(1, lights)
if lights != target:
    result_2 = -1

if result_1 == -1:
    print(result_2)
elif result_2 == -1:
    print(result_1)
else:
    print(min(result_1, result_2))
