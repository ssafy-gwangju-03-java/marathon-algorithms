# 2239 스도쿠

lst = [list(map(int, input())) for _ in range(9)]


def check_row(r):
    chk = [0] * (10)
    for i in range(9):
        chk[lst[r][i]] += 1
    for i in range(1, 10):
        if chk[i] > 1:
            return True
    return False


def check_col(c):
    chk = [0] * (10)
    for i in range(9):
        chk[lst[i][c]] += 1
    for i in range(1, 10):
        if chk[i] > 1:
            return True
    return False


def check_sq(r, c):
    chk = [0] * (10)
    rr = (r // 3) * 3
    cc = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            chk[lst[rr + i][cc + j]] += 1
    for i in range(1, 10):
        if chk[i] > 1:
            return True
    return False


def dfs(r, c):
    # 가로 끝으로 가면 다음 줄로 넘어감
    if c == 9:
        r += 1
        c = 0
        # 마지막 끝점의 경우
        if r == 9:
            return True

    # 있으면 패스
    if lst[r][c] != 0:
        return dfs(r, c + 1)

    for i in range(1, 10):
        lst[r][c] = i
        if not check_row(r) and not check_col(c) and not check_sq(r, c):
            if dfs(r, c + 1):
                return True

    lst[r][c] = 0
    return False


dfs(0, 0)
for i in range(9):
    for j in range(9):
        print(lst[i][j], end="")
    print()
