# https://www.acmicpc.net/problem/17144

## Referenced
# https://velog.io/@seungjae/백준-17144번-미세먼지-안녕-삼성-SW역량테스트-Python

import sys

input = sys.stdin.readline


def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C


def dust_spread():
    while status:
        # 미세먼지 위치 확인
        r, c, dust = status.pop()
        count = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 확산 위치에 청정기가 없다면 확산
            if is_valid(nr, nc) and (nr, nc) not in purifier:
                room[nr][nc] += dust // 5
                count += 1
        room[r][c] -= (dust // 5) * count


def purify(purifier):
    # 위에 회전
    r, c = purifier[0][0], 1
    i = 1 # 우 상 좌 하 이동
    temp = 0  # 미세먼지 이동용 스왑 변수

    while True:
        nr, nc = r + dr[i], c + dc[i]
        # 맵 밖으로 나갈 경우 방향 전환
        if nr == R or nc == C or nr == -1 or nc == -1:
            i = (i - 1) % 4
            continue
        # 청정기를 만났을 경우 종료
        if r == purifier[0][0] and c == 0:
            break

        # 스왑을 통해 미세먼지를 이동시킴
        room[r][c], temp = temp, room[r][c]
        r, c = nr, nc

    # 아래 회전
    r, c = purifier[1][0], 1
    i = 1 # 우 하 좌 상 이동
    temp = 0

    while True:
        nr, nc = r + dr[i], c + dc[i]
        if nr == R or nc == C or nr == -1 or nc == -1:
            i = (i + 1) % 4
            continue
        if r == purifier[1][0] and c == 0:
            break

        room[r][c], temp = temp, room[r][c]
        r, c = nr, nc


# 하 우 상 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

status = []
purifier = []

# 정화 시작 전 맵 구조 파악
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            status.append((r, c, room[r][c]))
        if room[r][c] == -1:
            purifier.append((r, c))

for t in range(T):
    dust_spread()
    purify(purifier)

    # 정화 후 맵 구조 파악
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                status.append((r, c, room[r][c]))

print(sum(status[i][2] for i in range(len(status))))
