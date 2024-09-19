# https://www.acmicpc.net/problem/3190

## Referenced
# https://ji-gwang.tistory.com/473

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

# 사과 위치 설정
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

# 시간별 회전 정보 저장할 딕셔너리
L = int(input())
time_dict = {}
for _ in range(L):
    X, C = input().split()
    time_dict[int(X)] = C

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c, di, time = 0, 0, 0, 0
snake = deque()

while True:
    # 뱀의 현재 위치 저장
    snake.append((r, c))
    time += 1

    r += d[di][0]
    c += d[di][1]

    # 벽에 부딪히거나 자기 몸과 부딪히면
    if r < 0 or r >= N or c < 0 or c >= N or arr[r][c] == 2:
        break

    # 사과가 없다면 꼬리 삭제
    if not arr[r][c]:
        i, j = snake.popleft()
        arr[i][j] = 0

    # 사과 먹은 후 몸길이 증가
    arr[r][c] = 2

    if time in time_dict:
        # 오른쪽으로 회전
        if time_dict[time] == "D":
            di = (di + 1) % 4
        # 왼쪽으로 회전
        else:
            di = (di - 1) % 4

print(time)
