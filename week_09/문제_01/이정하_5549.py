# M*N map
M, N = map(int, input().split())
# 조사대상 영역 개수 K
K = int(input())

# 지도 내용 - 지형 정글J, 바다O, 얼음I
geo = [list(input()) for _ in range(M)]
# 조사 대상 영역 K개의 정보
# a b c d => (x1,y1),(x2,y2) 순서로 주어짐
area = [list(map(int, input().split())) for _ in range(K)]

# 누적합 개수 저장할 리스트
# res[n][m][0~2] => [n]번쨰 col, [m]번째 row의 정보(0번 칸에는 정글J, 1번칸은 바다O, 2번칸은 얼음I)
result = [[[0] * 3 for _ in range(N + 1)] for _ in range(M + 1)]

# 1. 누적합 구하기
for r in range(1, M + 1):
    for c in range(1, N + 1):
        result[r][c][0] = (result[r - 1][c][0] + result[r][c - 1][0] - result[r - 1][c - 1][0]
                           + (1 if geo[r - 1][c - 1] == 'J' else 0))
        result[r][c][1] = (result[r - 1][c][1] + result[r][c - 1][1] - result[r - 1][c - 1][1]
                           + (1 if geo[r - 1][c - 1] == 'O' else 0))
        result[r][c][2] = (result[r - 1][c][2] + result[r][c - 1][2] - result[r - 1][c - 1][2]
                           + (1 if geo[r - 1][c - 1] == 'I' else 0))
    # print(result[r])
# 2. (x2,y2)까지의 누적합 + (x1,y1)까지의 누적합(중복되니까) - (x1,y2)누적합 - (y1,x2)누적합
for x1, y1, x2, y2 in area:
    # print(x1, y1, '/', x2, y2)
    # x2 -= 1
    # x1 -= 1
    j_cnt = result[x2][y2][0] + result[x1-1][y1-1][0] - result[x1-1][y2][0] - result[x2][y1-1][0]
    o_cnt = result[x2][y2][1] + result[x1-1][y1-1][1] - result[x1-1][y2][1] - result[x2][y1-1][1]
    i_cnt = result[x2][y2][2] + result[x1-1][y1-1][2] - result[x1-1][y2][2] - result[x2][y1-1][2]
    # print()
    print(j_cnt, o_cnt, i_cnt)
