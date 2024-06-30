import sys
from collections import deque
from itertools import product

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 0: 상, 1: 좌, 2: 하, 3: 우
# 4개의 방향으로 움직이는 경우의 수를 5번 중복으로 뽑기 (중복순열)
orders = product([0, 1, 2, 3], repeat=5)


# 한 줄의 숫자를 정리해주는 함수
# arr == 검사를 진행할 행 혹은 열 (1차원 배열)
def arrange(arr, range_obj):
    # 검사를 진행 할 숫자들
    to_check = deque()

    # 검사가 완료된 숫자들
    checked = deque()

    for i in range_obj:
        if arr[i]:
            if not to_check:
                to_check.append(arr[i])
            else:
                prev = to_check.pop()
                if arr[i] == prev:
                    # 같은 숫자를 만나면 *2 해주고 to_check에 있던 숫자들은 전부 검사 완료 처리
                    while to_check:
                        checked.append(to_check.popleft())
                    checked.append(prev * 2)
                else:
                    # 같은 숫자 아니면 to_check에 다시 넣어주기
                    to_check.append(prev)
                    to_check.append(arr[i])

    # to_check에 남아있는 숫자가 있다면 완료 처리
    while to_check:
        checked.append(to_check.popleft())

    return checked


# 특정 방향(d == direction)으로 숫자들을 1회 미는 게임 진행 함수
# d의 반대 방향으로 검사한 후 순서대로 *2, 혹은 다시 쌓아서 넣어주기
def play(arr, d):
    if d == 0:
        for j in range(N):
            # 검사 진행할 행렬 만들기
            to_check = [0] * N
            for i in range(N):
                to_check[i] = arr[i][j]
            checked = arrange(to_check, range(N))

            # 검사 완료 된 숫자들로 배열 갱신
            for i in range(N):
                if checked:
                    arr[i][j] = checked.popleft()
                else:
                    arr[i][j] = 0

    # 이하 방향만 바꿔서 같은 로직으로 검사
    elif d == 1:
        for i in range(N):
            checked = arrange(arr[i], range(N))

            for j in range(N):
                if checked:
                    arr[i][j] = checked.popleft()
                else:
                    arr[i][j] = 0

    elif d == 2:
        for j in range(N):
            to_check = [0] * N
            for i in range(N):
                to_check[i] = arr[i][j]
            checked = arrange(to_check, range(N - 1, -1, -1))

            for i in range(N - 1, -1, -1):
                if checked:
                    arr[i][j] = checked.popleft()
                else:
                    arr[i][j] = 0

    elif d == 3:
        for i in range(N):
            checked = arrange(arr[i], range(N - 1, -1, -1))

            for j in range(N - 1, -1, -1):
                if checked:
                    arr[i][j] = checked.popleft()
                else:
                    arr[i][j] = 0


max_block = 0

# 4개의 방향으로 움직이는 경우의 수를 5번 중복으로 뽑아놓은 순서를 가져와 완전탐색
for order in orders:
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]

    for d in order:
        play(new_board, d)

    max_block = max(max_block, max(map(max, new_board)))

print(max_block)



# N = 4
# arr = [
#     [2, 4, 16, 8],
#     [8, 4, 0, 0],
#     [16, 8, 2, 0],
#     [2, 8, 2, 0]
# ]
#
# play(arr, 0)
# for i in range(len(arr)):
#     print(arr[i])
