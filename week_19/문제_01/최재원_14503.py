import sys

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.read

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def clean(r, c, current_direction, arr, N, M):
    answer = 0

    while True:
        # 현재 칸이 아직 청소되지 않은 경우 청소
        if arr[r][c] == 0:
            arr[r][c] = 2
            answer += 1

        # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        if find_uncleaned_area(r, c, arr, N, M):
            # 반시계 방향 회전
            current_direction = (current_direction + 1) % 4

            nr = r + dr[current_direction]
            nc = c + dc[current_direction]

            if in_range(nr, nc, N, M) and arr[nr][nc] == 0:
                r = nr
                c = nc
        else:
            # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            reverse_direction = (current_direction + 2) % 4
            nr = r + dr[reverse_direction]
            nc = c + dc[reverse_direction]

            if in_range(nr, nc, N, M) and arr[nr][nc] != 1:
                r = nr
                c = nc
            else:
                break

    return answer


def find_uncleaned_area(r, c, arr, N, M):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if in_range(nr, nc, N, M):
            if arr[nr][nc] == 0:
                return True

    return False


def in_range(r, c, N, M):
    return 0 <= r < N and 0 <= c < M

data = input().splitlines()
N, M = map(int, data[0].split())
r, c, d = map(int, data[1].split())
arr = [list(map(int, line.split())) for line in data[2:2 + N]]

if d == 0:
    current_direction = 0
elif d == 1:
    current_direction = 3
elif d == 2:
    current_direction = 2
else:
    current_direction = 1

answer = clean(r, c, current_direction, arr, N, M)
print(answer)

