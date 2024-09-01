# b3190 뱀
from collections import deque

# 보드 크기
N = int(input())

# 게임 보드
lst = [[0] * N for _ in range(N)]
# 처음 뱀의 위치
lst[0][0] = 1

# 사과 개수 K
K = int(input())

# 사과 위치
# 1행 1열로 시작 -1 해주기
for _ in range(K):
    a, b = map(int, input().split())
    lst[a-1][b-1] = -1

# 방향 변환 정보 L개
L = int(input())
# 초
time_lst = []
# 이동 방향
move_lst = [0] * 10001
for _ in range(L):
    a, b = input().split()
    # X초가 끝난 후니까 X+1 초 부터 전환한 방향으로 이동
    time_lst.append(int(a) + 1)
    move_lst[int(a) + 1] = b

t = 0
# 방향 정보
d = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 뱀의 있는 위치 담은 deque
q = deque([(0, 0)])

while True:
    t += 1
    # 방향 바꾸는 시간일 때 방향 바꿔주기
    if t in time_lst:
        if move_lst[t] == "D":
            d = (d + 1) % 4
        elif move_lst[t] == "L":
            d = (d - 1)
            if d == -1:
                d = 3

    # 뱀의 머리
    sr, sc = q[-1]

    # 방향에 맞게 이동
    r = sr+dr[d]
    c = sc+dc[d]

    # 보드의 범위 내인지 확인
    if 0 <= r < N and 0 <= c < N:
        # 사과 있으면 뱀의 머리만 이동
        if lst[r][c] == -1:
            # 머리 이동
            lst[r][c] = 1
            q.append((r, c))
        # 사과가 없으면 뱀의 머리와 꼬리 이동
        elif lst[r][c] == 0:
            # 머리 이동
            lst[r][c] = 1
            q.append((r, c))
            # 꼬리 이동
            hr, hc = q.popleft()
            lst[hr][hc] = 0
        # 뱀의 몸과 닿으면 반복문 탈출
        elif lst[r][c] == 1:
            break
    # 보드 벗어나면 반복문 탈출
    else:
        break

# 게임이 끝날때까지 걸린 시간 출력
print(t)