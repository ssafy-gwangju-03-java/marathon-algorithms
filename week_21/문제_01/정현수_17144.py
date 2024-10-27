import sys

input = sys.stdin.read().splitlines()
R, C, T = map(int, input[0].split())
room = [list(map(int, line.split())) for line in input[1:]]

air_cleaner = []
for r in range(R):
    if room[r][0] == -1:
        air_cleaner.append(r)

def spread_dust():
    new_room = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                spread_amount = room[r][c] // 5
                spread_count = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        new_room[nr][nc] += spread_amount
                        spread_count += 1
                new_room[r][c] += room[r][c] - spread_amount * spread_count
    # 공기청정기 위치는 그대로 유지
    new_room[air_cleaner[0]][0] = -1
    new_room[air_cleaner[1]][0] = -1
    return new_room

def operate_air_cleaner():
    # 위쪽 반시계방향 순환
    top = air_cleaner[0]
    for r in range(top - 1, 0, -1):
        room[r][0] = room[r - 1][0]
    for c in range(C - 1):
        room[0][c] = room[0][c + 1]
    for r in range(top):
        room[r][C - 1] = room[r + 1][C - 1]
    for c in range(C - 1, 1, -1):
        room[top][c] = room[top][c - 1]
    room[top][1] = 0

    # 아래쪽 시계방향 순환
    bottom = air_cleaner[1]
    for r in range(bottom + 1, R - 1):
        room[r][0] = room[r + 1][0]
    for c in range(C - 1):
        room[R - 1][c] = room[R - 1][c + 1]
    for r in range(R - 1, bottom, -1):
        room[r][C - 1] = room[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        room[bottom][c] = room[bottom][c - 1]
    room[bottom][1] = 0

for _ in range(T):
    room = spread_dust()
    operate_air_cleaner()

ans = sum(sum(cell for cell in row if cell > 0) for row in room)
print(ans)
