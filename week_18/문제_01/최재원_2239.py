import sys

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = 9
arr = [list(map(int, input().strip())) for _ in range(N)]


def check_row_duplicate(r):
    counting_arr = [0] * (N + 1)
    for i in range(N):
        counting_arr[arr[r][i]] += 1
    for i in range(1, N + 1):
        if counting_arr[i] >= 2:
            return True
    return False

def check_col_duplicate(c):
    counting_arr = [0] * (N + 1)
    for i in range(N):
        counting_arr[arr[i][c]] += 1
    for i in range(1, N + 1):
        if counting_arr[i] >= 2:
            return True
    return False


# 3*3 네모난 모양에 겹치는 수가 있는지 판단
def check_square_duplicate(r, c):
    counting_arr = [0] * (N + 1)
    sr = (r // 3) * 3
    sc = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            counting_arr[arr[sr + i][sc + j]] += 1
    for i in range(1, N + 1):
        if counting_arr[i] >= 2:
            return True
    return False


def dfs(r, c):
    # 열의 끝에 닿으면 다음 행으로 넘어간다
    if c == N:
        r += 1
        c = 0
        # 마지막 열, 마지막 행을 탐색했으면 해답을 찾은 경우
        if r == N:
            return True

    # 이미 채워져있는 칸이면 다음 칸으로 넘어가기
    if arr[r][c] != 0:
        return dfs(r, c + 1)

    # 1부터 9까지 넣기
    for i in range(1, 10):
        arr[r][c] = i
        # 스도쿠 규칙에 유효하면
        if not check_row_duplicate(r) and not check_col_duplicate(c) and not check_square_duplicate(r, c):
            # 다음 칸으로 이동
            if dfs(r, c + 1):
                # 정답을 만들면 True
                return True

    # 1부터 10까지 다 넣어봐도 정답을 못만들었으면 백트래킹
    arr[r][c] = 0
    return False


dfs(0, 0)
for row in arr:
    print("".join(map(str, row)))
