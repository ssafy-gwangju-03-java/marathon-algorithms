# 3190 뱀
from collections import deque
import sys

input = sys.stdin.readline
# D +1 L -1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
k = int(input())
lst = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    lst[r - 1][c - 1] = 2  # 사과
lst[0][0] = 1  # 뱀

l = int(input())
go = []  # 시간,방향
for _ in range(l):
    x, c = map(str, input().split())
    go.append((int(x), c))
game = deque(go)  # 명령 저장소
cnt = 0
snake = deque()
snake.append((0, 0))  # 뱀 저장소
head = [0, 0]
dir = 0
X, C = game.popleft()
while 1:
    cnt += 1
    x, y = head
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and lst[ny][nx] != 1: # 범위 내, 뱀이 아닌 영역일때만 진행 가능
        if lst[ny][nx] == 2:  # 사과 있으면 먹고 길이+1
            lst[ny][nx] = 1
            head = [nx, ny]
            snake.appendleft(head)
        else:  # 없으면 앞으로 간다음 꼬리 빼기
            lst[ny][nx] = 1
            head = [nx, ny]
            snake.appendleft(head)
            r, c = snake.pop()
            lst[c][r] = 0
    else:
        break
    if X == cnt:
        if C == "D":
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        if game:
            X, C = game.popleft()
print(cnt)
