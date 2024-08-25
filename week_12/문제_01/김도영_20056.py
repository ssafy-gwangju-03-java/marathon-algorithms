# 마법사 상어와 파이어볼

N, M, K = map(int, input().split())

# r, c, m, s, d
# r, c: 위치 -> j, i
# m: 질량
# s: 속도
# d: 방향
fireballs = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[r - 1][c - 1].append((r - 1, c - 1, m, s, d))

# 방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


# 파이어볼 이동
def move(fireballs):
    new_fireballs = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if fireballs[i][j]:
                for fireball in fireballs[i][j]:
                    r, c, m, s, d = fireball

                    nr = (r + dr[d] * s) % N
                    nc = (c + dc[d] * s) % N

                    new_fireballs[nr][nc].append((nr, nc, m, s, d))

    return new_fireballs


# 파이어볼 합쳐짐
def add(fireballs):
    new_fireballs = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(fireballs[i][j]) >= 2:
                fireball_cnt = len(fireballs[i][j])
                new_m = 0
                new_s = 0
                new_d = 0

                for fireball in fireballs[i][j]:
                    new_m += fireball[2]
                    new_s += fireball[3]
                    new_d += (fireball[4] % 2)

                new_m //= 5
                new_s //= fireball_cnt

                if new_m == 0:
                    continue

                if new_m > 0:
                    # 새 방향 설정 (짝수 방향 또는 홀수 방향)
                    if new_d in [0, fireball_cnt]:
                        for d in [0, 2, 4, 6]:
                            new_fireballs[i][j].append((i, j, new_m, new_s, d))
                    else:
                        for d in [1, 3, 5, 7]:
                            new_fireballs[i][j].append((i, j, new_m, new_s, d))
            else:
                new_fireballs[i][j] = fireballs[i][j]

    return new_fireballs


for _ in range(K):
    fireballs = move(fireballs)
    fireballs = add(fireballs)

result = 0
for i in range(N):
    for j in range(N):
        for fireball in fireballs[i][j]:
            result += fireball[2]

print(result)