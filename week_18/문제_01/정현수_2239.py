def calculate_square_index(x, y):
    # (x, y) 좌표가 속하는 3x3 정사각형 인덱스 계산
    return (x // 3) * 3 + (y // 3)


def solve_sudoku(n):
    if n == 81:
        for row in board:
            print(''.join(map(str, row)))
        return 1

    # n => (x, y)
    x = n // 9
    y = n % 9

    # 이미 채워진 칸이면 다음 칸으로 이동
    if board[x][y] != 0:
        return solve_sudoku(n + 1)

    for num in range(1, 10):
        square_index = calculate_square_index(x, y)

        # 해당 숫자가 해당 행, 열, 3x3 박스에서 사용되지 않았으면
        if not row_check[x][num] and not col_check[y][num] and not square_check[square_index][num]:
            
            row_check[x][num] = col_check[y][num] = square_check[square_index][num] = 1
            board[x][y] = num

            if solve_sudoku(n + 1):
                return 1

            board[x][y] = 0
            row_check[x][num] = col_check[y][num] = square_check[square_index][num] = 0

    # 해결되지 않은 경우
    return 0


# 스도쿠 판 입력
board = [list(map(int, input().strip())) for _ in range(9)]

# 각 행, 열, 3x3 정사각형에서 숫자 사용 여부 체크
row_check = [[0] * 10 for _ in range(9)]  # 각 행에서 숫자 사용 여부
col_check = [[0] * 10 for _ in range(9)]  # 각 열에서 숫자 사용 여부
square_check = [[0] * 10 for _ in range(9)]  # 각 3x3 정사각형에서 숫자 사용 여부

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            num = board[i][j]
            row_check[i][num] = 1
            col_check[j][num] = 1
            square_check[calculate_square_index(i, j)][num] = 1

solve_sudoku(0)
