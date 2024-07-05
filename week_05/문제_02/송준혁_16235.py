# https://www.acmicpc.net/problem/16235

import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = [[5] * N for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]

# 특정 위치에 심어진 나무들의 나이를 저장한 배열을 원소로 하는 2차원 배열
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r - 1][c - 1].append(age)

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def spring_summer():
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                # (r, c)에 심어진 나무들을 나이순 정렬 후, 영양분이 충분하면 나이++
                # 영양분이 부족하면 반복 중단, 영양 부족한 나무 개수만큼 pop 후 영양++

                # 봄
                trees[r][c].sort()
                tree_count = 0
                for idx, tree in enumerate(trees[r][c]):
                    if tree <= grid[r][c]:
                        grid[r][c] -= tree
                        trees[r][c][idx] += 1
                        tree_count += 1
                    else:
                        break

                # 여름
                if tree_count != len(trees[r][c]):
                    for _ in range(len(trees[r][c]) - tree_count):
                        age = trees[r][c].pop()
                        grid[r][c] += age // 2


def autumn_winter():
    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N

    for r in range(N):
        for c in range(N):
            # 가을
            if trees[r][c]:
                for tree in trees[r][c]:
                    if tree % 5 == 0:
                        for i in range(8):
                            nr, nc = r + d[i][0], c + d[i][1]
                            if is_valid(nr, nc):
                                trees[nr][nc].append(1)
            # 겨울
            grid[r][c] += s2d2[r][c]


for k in range(K):
    spring_summer()
    autumn_winter()

count = 0
for r in range(N):
    for c in range(N):
        count += len(trees[r][c])

print(count)
