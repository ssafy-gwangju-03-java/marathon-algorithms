import sys

R, C = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# J, O, I 별로 누적합 구해줄 2차원 배열
acc = [[{"J": 0, "O": 0, "I" : 0} for _ in range(C + 1)] for _ in range(R + 1)]

# 오른쪽 방향으로 누적합
for i in range(1, R + 1):
    first_char = board[i - 1][0]
    acc[i][1][first_char] += 1

    for j in range(2, C + 1):
        acc[i][j]["J"] = (acc[i][j - 1]["J"] + int(board[i - 1][j - 1] == "J"))
        acc[i][j]["O"] = (acc[i][j - 1]["O"] + int(board[i - 1][j - 1] == "O"))
        acc[i][j]["I"] = (acc[i][j - 1]["I"] + int(board[i - 1][j - 1] == "I"))

# 아래 방향으로 누적합
for j in range(1, C + 1):
    for i in range(2, R + 1):
        acc[i][j]["J"] = acc[i - 1][j]["J"] + acc[i][j]["J"]
        acc[i][j]["O"] = acc[i - 1][j]["O"] + acc[i][j]["O"]
        acc[i][j]["I"] = acc[i - 1][j]["I"] + acc[i][j]["I"]

# 조사 영역 누적합 구하기
for _ in range(K):
    sr, sc, er, ec = map(int, sys.stdin.readline().split())
    for char in "JOI":
        print(acc[er][ec][char] - acc[er][sc - 1][char] - acc[sr - 1][ec][char] + acc[sr - 1][sc - 1][char], end=" ")
    print()