# 드래곤 커브

N = int(input())

# [x, y, d, g]
# x, y : 시작점
# d : 시작 방향
# g : 세대
curve_lst = [list(map(int, input().split())) for _ in range(N)]

board = [[0] * 101 for _ in range(101)]

# [0, 1, 2, 3]
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def curve(curve_info):
    # 현재 위치
    # 좌표랑 인덱스 반대인거 주의
    i, j = curve_info[1], curve_info[0]
    # 시작점 처리
    board[i][j] = 1

    # 현재 세대
    now_gen = 0

    # 도달해야 하는 세대
    gen = curve_info[3]

    direction = [curve_info[2]]

    while now_gen < gen:
        now_gen += 1
        new_direction = direction[:]
        direction.reverse()

        for d in direction:
            new_direction.append((d + 1) % 4)
        
        direction = new_direction
    
    # print(direction)
    # print(i, j)
    for d in direction:
        i += di[d]
        j += dj[d]

        board[i][j] = 1
        # print(i, j)
    
    # print()

for curve_info in curve_lst:
    curve(curve_info)

# 우 하 우하
ni = [0, 1, 1]
nj = [1, 0, 1]
def square(si, sj):
    for n in range(3):
        ci = si + ni[n]
        cj = sj + nj[n]
        
        if board[ci][cj] != 1:
            return False
    
    return True

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            # print(i, j)
            result = square(i, j)

            if result == True:
                cnt += 1

print(cnt)