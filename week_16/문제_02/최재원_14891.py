import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

gears = []
for _ in range(4):
    gears.append(deque(map(int, input().strip())))

K = int(input())


# 톱니바퀴 사이가 연결되어있는지 확인
def update_connection():
    connection = [False] * 3
    for i in range(3):
        if gears[i][2] != gears[i + 1][6]:
            connection[i] = True
    return connection

# 회전시키기
def rotate(num, direction):
    # 1이면 시계방향, -1이면 반시계
    gears[num].rotate(direction)


for _ in range(K):
    num, direction = map(int, input().split())
    num -= 1

    connection = update_connection()

    # 돌릴 방향 저장할 배열
    rotate_directions = [0] * 4
    # 돌려지는 타겟 톱니바퀴의 돌릴 방향 저장
    rotate_directions[num] = direction

    # 타겟 톱니바퀴의 왼쪽 톱니바퀴가 이어져 있으면
    for i in range(num - 1, -1, -1):
        if connection[i]:
            rotate_directions[i] = -rotate_directions[i + 1]
        else:
            break

    # 타겟 톱니바퀴의 오른쪽 톱니바퀴가 이어져 있으면
    for i in range(num + 1, 4):
        if connection[i - 1]:
            rotate_directions[i] = -rotate_directions[i - 1]
        else:
            break

    # 톱니바퀴 돌리기
    for i in range(4):
        if rotate_directions[i] != 0:
            rotate(i, rotate_directions[i])

answer = 0
for i in range(4):
    if gears[i][0] == 1:
        answer += (2 ** i)

print(answer)
