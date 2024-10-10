import sys

R, C = map(int, sys.stdin.readline().split())
cr, cc, cd = map(int, sys.stdin.readline().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

cleaned = 0

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not room[cr][cc]:
        room[cr][cc] = 2
        cleaned += 1

    all_cleaned = True

    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if room[nr][nc] == 0:
            all_cleaned = False
            break

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if all_cleaned:
        # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
        cr += dr[(cd - 2) % 4]
        cc += dc[(cd - 2) % 4]
        # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if room[cr][cc] == 1:
            break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        for _ in range(4):
            # 3-1. 반시계 방향으로 90도 회전
            cd = (cd - 1) % 4
            # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            nr, nc = cr + dr[cd], cc + dc[cd]
            if not room[nr][nc]:
                cr, cc = nr, nc
                break

print(cleaned)

