# 뱀

from collections import deque
from pprint import pprint

# N x N 보드
N = int(input())

board = [[0] * N for _ in range(N)]
board[0][0] = 1

# 사과의 개수
K = int(input())

# 사과의 위치(행, 열)
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

# 뱀의 방향 변환 횟수
L = int(input())

# 뱀의 방향 변환 정보
snake = deque()
for _ in range(L):
    X, C = input().split()
    snake.append([int(X), C])

# 방향전환
# 오른쪽으로 돌 때 기준
# 오른쪽(D)일때는 +1, 왼쪽(L)일때는 -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 방향, 머리 위치
snake_dir = 0
snake_head = [0, 0]

# 게임 진행 시간
time = 0

# 뱀이 있는 위치를 기억할 deque
# 앞이 머리, 뒤가 꼬리
snake_pos = deque()
snake_pos.append(snake_head)

X, C = snake.popleft()

while True:
    time += 1

    # 뱀의 머리 위치
    x, y = snake_head

    # 뱀의 머리 이동
    nx = x + dx[snake_dir]
    ny = y + dy[snake_dir]

    # 벽에 부딪히거나 자기 자신의 몸에 부딪히면 게임 종료
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
        break

    # 사과가 있는 경우
    if board[nx][ny] == 2:
        board[nx][ny] = 1
        snake_head = [nx, ny]
        snake_pos.appendleft(snake_head)
    
    # 사과가 없는 경우
    else:
        board[nx][ny] = 1
        snake_head = [nx, ny]
        snake_pos.appendleft(snake_head)

        # 몸길이 줄여서 꼬리 이동
        tail = snake_pos.pop()
        board[tail[0]][tail[1]] = 0

    # 뱀이 방향전환을 하는 시간
    if X == time:
        if C == 'D':
            snake_dir = (snake_dir + 1) % 4

        elif C == 'L':
            snake_dir = (snake_dir - 1) % 4
        
        if snake:
            X, C = snake.popleft()

print(time)