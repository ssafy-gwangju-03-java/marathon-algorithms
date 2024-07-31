import sys
sys.stdin = open("../../input.txt", 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

field = [list(input().strip()) for _ in range(N)]
search_range = [list(map(int, input().split())) for _ in range(K)]

# acc[i][j][0]은 (0,0)에서부터 (i,j)까지 정글J 누적합
# acc[i][j][1]은 (0,0)에서부터 (i,j)까지 바다O 누적합
# acc[i][j][2]은 (0,0)에서부터 (i,j)까지 얼음I 누적합
acc = [[[0 for _ in range(3)] for _ in range(M + 1)] for _ in range(N + 1)]

# 누적합 구하기
for i in range(N):
    for j in range(M):
        # 이전 누적합으로부터 현재 누적합 구하기
        # (i,j)까지의 누적합은 (0, 0)부터 (i - 1, j)까지의 누적합 + (0, 0)부터 (i, j - 1)까지의 누적합 - (i - 1, j - 1)까지의 누적합
        acc[i + 1][j + 1][0] = acc[i][j + 1][0] + acc[i + 1][j][0] - acc[i][j][0]
        acc[i + 1][j + 1][1] = acc[i][j + 1][1] + acc[i + 1][j][1] - acc[i][j][1]
        acc[i + 1][j + 1][2] = acc[i][j + 1][2] + acc[i + 1][j][2] - acc[i][j][2]

        # 현재 칸에 따라 누적합 증가
        if field[i][j] == 'J':
            acc[i + 1][j + 1][0] += 1
        elif field[i][j] == 'O':
            acc[i + 1][j + 1][1] += 1
        elif field[i][j] == 'I':
            acc[i + 1][j + 1][2] += 1

# 누적합 배열을 가지고 조사 대상 영역의 정글, 바다, 얼음 수 구하기
for r1, c1, r2, c2 in search_range:
    # 전체 사각형에서 위쪽 사각형과 왼쪽 사각형을 빼고 두번 빼진 왼쪽 위 사각형 더하기
    J = acc[r2][c2][0] - acc[r1 - 1][c2][0] - acc[r2][c1 - 1][0] + acc[r1 - 1][c1 - 1][0]
    O = acc[r2][c2][1] - acc[r1 - 1][c2][1] - acc[r2][c1 - 1][1] + acc[r1 - 1][c1 - 1][1]
    I = acc[r2][c2][2] - acc[r1 - 1][c2][2] - acc[r2][c1 - 1][2] + acc[r1 - 1][c1 - 1][2]
    print(J, O, I)

