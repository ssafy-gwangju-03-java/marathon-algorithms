# 2239 스도쿠
import sys
input = sys.stdin.readline
# 빈칸 찾기
def where_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

# 행/열/3*3 확인
def check(sudoku, num, current):
    # 행
    for j in range(9):
        if sudoku[current[0]][j] == num and current[1] != j:
            return False

    # 열
    for i in range(9):
        if sudoku[i][current[1]] == num and current[0] != i:
            return False

    # 3*3
    xBox = current[1] // 3
    yBox = current[0] // 3

    for i in range(yBox*3, yBox*3+3):
        for j in range(xBox*3, xBox*3+3):
            if sudoku[i][j] == num and (i, j) != current:
                return False

    return True

# 스도쿠 ㄱㄱ
def solve(sudoku):
    empty = where_empty(sudoku)
    if not empty:
        return True
    r, c = empty

    for n in range(1, 10):
        if check(sudoku, n, (r, c)):
            sudoku[r][c] = n

            if solve(sudoku):
                return True

            sudoku[r][c] = 0
    return False


sudoku = [list(map(int, input().strip())) for _ in range(9)]
solve(sudoku)
# 공백 없이 output(*로 comprehension 쓰면 공백때문에ㅠㅠㅠ)
for ans in sudoku:
    print(''.join(map(str, ans)))
