num = 9


# 가로 확인
def r_check(r, n):
    for c in range(num):
        # 중복 된 숫자가 있으면 false
        if lst[r][c] == n:
            return False
    return True


# 세로 확인
def c_check(c, n):
    for r in range(num):
        # 중복 된 숫자가 있으면 false
        if lst[r][c] == n:
            return False
    return True


# 3*3 배열 확인
def t_check(r, c, n):
    # 속한 3*3 배열에서 확인하기
    r = (r // 3) * 3
    c = (c // 3) * 3
    for k in range(3):
        for l in range(3):
            if lst[r+k][c+l] == n:
                return False
    return True


def dfs(idx):
    if idx == len(zero):
        for a in range(num):
            for b in range(num):
                print(lst[a][b], end="")
            print()
        exit()

    sr, sc = zero[idx]
    for n in range(1, num+1):
        if r_check(sr, n) and c_check(sc, n) and t_check(sr, sc, n):
            lst[sr][sc] = n
            dfs(idx + 1)
            lst[sr][sc] = 0


lst = [list(map(int, input().rstrip())) for _ in range(num)]
# print(lst)
zero = []

for i in range(num):
    for j in range(num):
        if lst[i][j] == 0:
            zero.append((i, j))


dfs(0)