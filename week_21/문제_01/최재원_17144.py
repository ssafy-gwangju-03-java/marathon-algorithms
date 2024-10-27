import sys

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]


def diffuse():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    diffused = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if arr[r][c] <= 0:
                continue

            dust = arr[r][c] // 5

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위 내에 있고 공기 청정기의 위치가 아닐 때
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                    diffused[nr][nc] += dust
                    diffused[r][c] -= dust

    # 확산된 양 반영
    for r in range(R):
        for c in range(C):
            arr[r][c] += diffused[r][c]


# 시계 방향
def clean_dust_up():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    r, c, direction = m1, 1, 0
    prev = 0

    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]

        if r == m1 and c == 0:
            break

        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            direction += 1
            continue

        arr[r][c], prev = prev, arr[r][c]
        r, c = nr, nc


# 반시계 방향
def clean_dust_down():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c, direction = m2, 1, 0
    prev = 0

    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 방향대로 모두 한칸씩 미뤘을 때
        if r == m2 and c == 0:
            break

        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            direction += 1
            continue

        arr[r][c], prev = prev, arr[r][c]
        r, c = nr, nc


# 공기청정기의 위치
for i in range(R):
    if arr[i][0] == -1:
        m1 = i
        m2 = i + 1
        break

for _ in range(T):
    diffuse()
    clean_dust_up()
    clean_dust_down()

answer = 0

for r in range(R):
    for c in range(C):
        if arr[r][c] > 0:
            answer += arr[r][c]

print(answer)
