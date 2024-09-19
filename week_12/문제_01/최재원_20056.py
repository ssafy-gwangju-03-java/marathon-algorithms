import sys
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

class FireBall:
    def __init__(self, r, c, m, s, d):
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d

    def __repr__(self):
        return str(self.r) + str(self.c) + str(self.m) + str(self.s) + str(self.d)

    def move(self):
        self.r = (self.r + dr[self.d] * self.s) % N
        self.c = (self.c + dc[self.d] * self.s) % N
        field[self.r][self.c].append(self)


field = [[[] for _ in range(N)] for _ in range(N)]

fire_balls = []
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls.append(FireBall(r - 1, c - 1, m, s, d))

for _ in range(K):
    # 파이어볼 움직이고 맵에 추가
    for fire_ball in fire_balls:
        fire_ball.move()

    # 파이어볼 초기화
    fire_balls = []

    # 파이어볼 합치기
    for i in range(N):
        for j in range(N):
            # 파이어볼이 2개 이상이면
            length = len(field[i][j])
            if length == 1:
                fire_balls.append(field[i][j][0])
            elif length >= 2:
                # 합치고 나누기
                sum_m = sum_s = 0
                even = odd = 0

                for fire_ball in field[i][j]:
                    sum_m += fire_ball.m
                    sum_s += fire_ball.s

                    if fire_ball.d % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                new_m = sum_m // 5
                new_s = sum_s // length

                if new_m > 0:
                    if even == 0 or odd == 0:
                        for d in (0, 2, 4, 6):
                            fire_balls.append(FireBall(i, j, new_m, new_s, d))
                    else:
                        for d in (1, 3, 5, 7):
                            fire_balls.append(FireBall(i, j, new_m, new_s, d))

    # 맵 초기화
    field = [[[] for _ in range(N)] for _ in range(N)]


answer = 0
for fire_ball in fire_balls:
    answer += fire_ball.m

print(answer)
