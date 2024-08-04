import sys

sys.stdin = open("../../input.txt", 'r')

input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(10)]
min_value = 26


def attachable(r, c, size, filled):
    # 범위 밖으로 넘어가면 못붙임
    if r + size > 10 or c + size > 10:
        return False
    # 색종이 범위에 0이 있으면 못붙임
    for i in range(r, r + size):
        for j in range(c, c + size):
            if filled[i][j] or arr[i][j] == 0:
                return False

    return True

# 색종이 붙이기/떼기 + 붙인부붙 True/ 뗀 부분 Falae
def attach(r, c, size, filled, status):
    for i in range(r, r + size):
        for j in range(c, c + size):
            filled[i][j] = status


def dfs(depth, filled, paper_count):
    global min_value

    # 색종이 개수가 현재 최솟값이 되면 백트래킹
    if depth == min_value:
        return

    for y in range(10):
        for x in range(10):
            if arr[y][x] == 1 and not filled[y][x]:
                # 큰 종이부터 붙이기
                for size in range(5, 0, -1):
                    # 남아있는 종이가 있고 붙일 수 있으면
                    if paper_count[size] > 0 and attachable(y, x, size, filled):
                        # 붙이고 종이 수 줄이기
                        attach(y, x, size, filled, True)
                        paper_count[size] -= 1

                        # 다음 색종이 붙이러 가기
                        dfs(depth + 1, filled, paper_count)

                        # 떼기
                        attach(y, x, size, filled, False)
                        paper_count[size] += 1
                return

    min_value = min(min_value, depth)


dfs(0, [[False] * 10 for _ in range(10)], [0, 5, 5, 5, 5, 5])

print(min_value if min_value != 26 else -1)
