import sys

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


N, M, K = map(int, sys.stdin.readline().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
ball_list = []


class Fireball:
    def __init__(self, r, c, m, s, d):
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d

    def __repr__(self):
        return f"(r: {self.r}, c: {self.c}, m: {self.m}, s: {self.s}, d: {self.d})"

    def move(self):
        self.r = (self.r + dr[self.d] * self.s) % N
        self.c = (self.c + dc[self.d] * self.s) % N


# 이동
def move():
    for i in range(N):
        for j in range(N):
            while grid[i][j]:
                fireball = grid[i][j].pop()
                fireball.move()

    for i in range(len(ball_list)):
        fireball = ball_list[i]
        grid[fireball.r][fireball.c].append(fireball)


# 4개로 쪼개기
def split_ball(r, c, m, s, rem):
    new_balls = []
    for d in range(8):
        if d % 2 == rem:
            fireball = Fireball(r, c, m, s, d)
            new_balls.append(fireball)
    return new_balls


# 합치기
def combine():
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) > 1:

                # 합쳐진 후 새롭게 생성될 파이어볼
                new_balls = []

                # floor(질량의 합 / 5)이 0이 아니라면 4개로 나눠진다
                new_mass = int(sum(map(lambda o: o.m, grid[i][j])) / 5)
                if new_mass > 0:
                    new_speed = int(sum(map(lambda o: o.s, grid[i][j])) / len(grid[i][j]))
                    rem = int(len(set(map(lambda o: o.d % 2, grid[i][j]))) != 1)
                    new_balls = split_ball(i, j, new_mass, new_speed, rem)

                # 기존의 fireball은 삭제해준다
                for fireball in grid[i][j]:
                    ball_list.remove(fireball)

                # 새롭게 생성된 4개의 파이어볼로 교체
                ball_list.extend(new_balls)
                grid[i][j] = new_balls


for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball = Fireball(r - 1, c - 1, m, s, d)
    grid[r - 1][c - 1].append(fireball)
    ball_list.append(fireball)


# K번 이동
for _ in range(K):
    move()
    combine()


answer = 0

for i in range(N):
    for j in range(N):
        for fireball in grid[i][j]:
            answer += fireball.m

print(answer)

