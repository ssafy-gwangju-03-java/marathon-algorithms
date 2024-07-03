import sys

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 양분을 저장해 줄 배열
nourishment = [[5] * N for _ in range(N)]


# tree_field[i][j] = [1, 2, 3]
# == i, j 위치에 존재하는 나이가 1, 2, 3인 나무
tree_field = [[[] for _ in range(N)] for _ in range(N)]


# 나무 입력
# (x, y) == (r, c)
for i in range(M):
    r, c, age = map(int, sys.stdin.readline().split())
    tree_field[r - 1][c - 1].append(age)


# K년 동안 사계절을 보낸다
for _ in range(K):

    # 봄
    for i in range(N):
        for j in range(N):

            # 나이가 어린 나무부터 양분을 먹는다
            tree_field[i][j].sort()

            for k in range(len(tree_field[i][j])):
                age = tree_field[i][j][k]

                if nourishment[i][j] >= age:
                    nourishment[i][j] -= age
                    tree_field[i][j][k] += 1

                # 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
                else:

                    # 여름
                    for tree in tree_field[i][j][k:]:
                        """
                        '//'를 '/'로 잘못써서 계속 틀림
                        파이썬은 '/'로 나누면 소수점 나옴 
                        floor하려면 '//'
                        """
                        nourishment[i][j] += tree // 2
                    tree_field[i][j] = tree_field[i][j][:k]
                    break


    # 가을
    for i in range(N):
        for j in range(N):
            for k in range(len(tree_field[i][j])):
                if tree_field[i][j][k] % 5 == 0:
                    for d in range(8):
                        nr, nc = i + dr[d], j + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            tree_field[nr][nc].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            nourishment[i][j] += A[i][j]


tree_count = 0

for i in range(N):
    for j in range(N):
        tree_count += len(tree_field[i][j])

print(tree_count)