import sys

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

# 배열에 1이 하나라도 남아있는지 확인하는 보조 함수
def leftover(arr):
    for i in range(10):
        for j in range(10):
            if arr[i][j]:
                return True
    return False

# 현재 size의 종이를 해당 영역에 붙일 수 있는지 확인하는 보조 함수
def check_full(arr, r, c, size):
    for i in range(size):
        for j in range(size):
            if r + i >= 10 or c + j >= 10 or not arr[r + i][c + j]:
                return False
    return True

# 색종이를 붙이거나 떼주는 보조 함수
# num == 0: (r, c)부터 size만큼의 색종이 붙이기
# num == 1: (r, c)부터 size만큼 색종이 떼기
def attach(arr, r, c, size, num):
    for i in range(size):
        for j in range(size):
            arr[r + i][c + j] = num
    return arr

def dfs(arr, count, paper_count):
    global min_count
    global paper

    # 이미 min_count가 나왔으면 백트래킹
    if count >= min_count:
        return

    # 1이 하나도 남지 않은 상태라면 (색종이 붙이기를 완료한 상황이라면) min_count 갱신
    if not leftover(arr):
        min_count = min(count, min_count)
        return

    for i in range(10):
        for j in range(10):
            if arr[i][j]:
                # 큰 사이즈의 종이부터 붙여보기
                # 큰 사이즈부터 먼저 다 붙일 수 있다면 최솟값을 빨리 찾을 수 있으니까
                for size in range(5, 0, -1):
                    if check_full(arr, i, j, size) and paper_count[size]:
                        attach(arr, i, j, size, 0)
                        paper_count[size] -= 1
                        dfs(arr, count + 1, paper_count)
                        paper_count[size] += 1
                        attach(arr, i, j, size, 1)
                return

min_count = 1000
dfs(paper, 0, [0, 5, 5, 5, 5, 5])
print(min_count if min_count != 1000 else -1)


# 오답 코드 :
# 큰 사이즈의 종이를 붙인 경우의 수와 그 다음 작은 사이즈의 종이를 붙여야 하는 경우의 수는 서로 유기적으로 연결되어있어야 한다
# https://steady-coding.tistory.com/43
#
# def dfs(size, arr, count, paper_count):
#     global max_count
#     global paper
#
#     if count <= max_count:
#         return
#
#     new_arr = [[0] * 10 for _ in range(10)]
#
#     for i in range(10):
#         for j in range(10):
#             new_arr[i][j] = arr[i][j]
#
#     did_attach = False
#
#     for i in range(10):
#         for j in range(10):
#             if new_arr[i][j]:
#                 if check_full(arr, i, j, size) and paper_count:
#                     did_attach = True
#                     attach(new_arr, i, j, size, 0)
#                     dfs(size, new_arr, count + 1, paper_count - 1)
#                     attach(new_arr, i, j, size, 1)
#
#     if not did_attach:
#         max_count = max(max_count, count)
#         paper = new_arr
#         return
#
# answer = 0
#
# for size in range(5, 0, -1):
#     max_count = -1
#     dfs(size, paper, 0, 5)
#     answer += max_count
#
# print(answer if not leftover(paper) else -1)
