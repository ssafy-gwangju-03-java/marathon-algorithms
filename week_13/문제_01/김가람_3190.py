import sys

# dr[0], dc[0] == 오른쪽 (초기 방향)
# index + 1 == 오른쪽으로 90도 회전
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 빈칸: 0, 사과: 1, 뱀: (direction, )
# direction == 뱀이 해당 칸을 지나갔을 당시의 방향
board = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 1

# 게임 시작 시 맨위 맨좌측에 위치하고 오른쪽(0)을 향한다
board[0][0] = (0,)

L = int(sys.stdin.readline())
change_dir = {}

for _ in range(L):
    X, C = sys.stdin.readline().split()
    if C == "D":
        change_dir[int(X)] = 1
    elif C == "L":
        change_dir[int(X)] = -1

d = 0           # 현재 방향
head = [0, 0]   # 머리의 위치
tail = [0, 0]   # 꼬리의 위치
sec = 0         # 초

while True:
    sec += 1

    # 머리 좌표 이동
    head[0] += dr[d]
    head[1] += dc[d]
    r, c = head[0], head[1]

    did_eat = False

    if not (0 <= r < N and 0 <= c < N) or type(board[r][c]) == tuple:
        print(sec)
        break
    elif board[r][c] == 1:
        did_eat = True

    # 해당 초가 끝나면 방향 회전
    d = (d + change_dir.get(sec, 0)) % 4

    # 머리가 위치한 곳에 지나간 당시의 방향 기록
    board[r][c] = (d,)

    # 사과를 먹지 않았다면 꼬리 지워주기
    if not did_eat:
        tr, tc = tail[0], tail[1]
        td = board[tr][tc][0]
        tail[0] += dr[td]
        tail[1] += dc[td]
        board[tr][tc] = 0
