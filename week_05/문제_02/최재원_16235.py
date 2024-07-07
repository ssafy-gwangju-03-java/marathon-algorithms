import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')

dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]


class Tree:
    def __init__(self, r, c, age):
        self.r = r
        self.c = c
        self.age = age

    def __str__(self):
        return f"{self.r} {self.c} {self.age}"

    def grow(self, nutrients):
        if nutrients[self.r][self.c] >= self.age:
            nutrients[self.r][self.c] -= self.age
            self.age += 1
            return True
        else:
            return False

    def die(self):
        return self.age // 2

    def reproduce(self):
        return self.age % 5 == 0


N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

field = [[deque() for _ in range(N)] for _ in range(N)]
nutrients = [[5] * N for _ in range(N)]

for _ in range(M):
    r, c, age = map(int, sys.stdin.readline().split())
    field[r - 1][c - 1].append(Tree(r - 1, c - 1, age))

for _ in range(K):
    # 봄, 여름
    dead_trees = []
    for r in range(N):
        for c in range(N):
            live_trees = deque()
            while field[r][c]:
                tree = field[r][c].popleft()
                if tree.grow(nutrients):
                    live_trees.append(tree)
                else:
                    dead_trees.append(tree)
            field[r][c] = live_trees

    for tree in dead_trees:
        nutrients[tree.r][tree.c] += tree.die()

    # 가을
    for r in range(N):
        for c in range(N):
            breed_count = 0
            for tree in field[r][c]:
                if tree.reproduce():
                    breed_count += 1
            if breed_count > 0:
                for d in range(8):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        for _ in range(breed_count):
                            field[nr][nc].appendleft(Tree(nr, nc, 1))

    # 겨울
    for r in range(N):
        for c in range(N):
            nutrients[r][c] += A[r][c]

answer = 0
for r in range(N):
    for c in range(N):
        answer += len(field[r][c])

print(answer)
