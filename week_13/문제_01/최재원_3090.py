import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
K = int(input())

# 사과 채우기
field = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    field[r - 1][c - 1] = 1

L = int(input())

commands = deque()
for _ in range(L):
    commands.append(list(input().split()))

time = 1
current_direction = 0
r, c = 0, 0
next_time, next_direction = commands.popleft()
snake = deque((r, c))

while True:
    # 시간이 되면 다음 초, 방향 받기
    if time == int(next_time) + 1:
        # 방향이 D(오른쪽)면 +1
        if next_direction == "D":
            current_direction = (current_direction + 1) % 4
        # 방향이 L(왼쪽)면 -1
        elif next_direction == "L":
            current_direction = (current_direction - 1) % 4

        # 다음 명령이 남아있으면 pop
        if commands:
            next_time, next_direction = commands.popleft()

    nr = r + dr[current_direction]
    nc = c + dc[current_direction]

    # 벽에 닿으면 끝
    if not (0 <= nr < N) or not (0 <= nc < N):
        break
    # 내 몸통에 닿으면 끝
    if (nr, nc) in snake:
        break
    # 이동한 칸에 사과가 있으면 머리만, 없으면 머리 추가하고 꼬리 지우기
    if field[nr][nc] == 1:
        field[nr][nc] = 0
        snake.append((nr, nc))
    else:
        snake.append((nr, nc))
        snake.popleft()

    # 현재 위치를 갱신하고 시간 증가
    r, c = nr, nc
    time += 1

print(time)
