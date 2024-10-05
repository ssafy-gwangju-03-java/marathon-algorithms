import sys

sudoku = [[0] * 9 for _ in range(9)]

# 가로, 세로, 3x3 사각형 체크할 배열
garo = [[] for _ in range(9)]
sero = [[] for _ in range(9)]
nemo = [[] for _ in range(9)]

# 입력과 동시에 위의 체크용 배열들에 넣어주기
for i in range(9):
    input_str = sys.stdin.readline()
    for j in range(9):
        curr = int(input_str[j])
        sudoku[i][j] = curr
        if curr:
            garo[i].append(curr)
            sero[j].append(curr)
            nemo[3 * (i // 3) + (j // 3)].append(curr)

# 백트래킹 함수
def dfs(r, c):
    global found_answer

    if found_answer:
        return

    # 마지막 행까지 다 채운 경우
    if r == 9:
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        found_answer = True
        return

    nr = r if c != 8 else r + 1
    nc = (c + 1) % 9

    # 이미 숫자가 있는 칸이면 넘어가고, 빈칸이면 숫자 채우기
    if sudoku[r][c]:
        dfs(nr, nc)
    else:
        for num in range(1, 10):
            if not (num in garo[r] or num in sero[c] or num in nemo[3 * (r // 3) + (c // 3)]):

                # 조건에 맞으면 숫자를 넣고 상태 업데이트
                sudoku[r][c] = num
                garo[r].append(num)
                sero[c].append(num)
                nemo[3 * (r // 3) + (c // 3)].append(num)

                # 다음 칸으로 이동
                dfs(nr, nc)

                # 복원 (backtracking)
                sudoku[r][c] = 0
                garo[r].pop()
                sero[c].pop()
                nemo[3 * (r // 3) + (c // 3)].pop()

found_answer = False
dfs(0, 0)



