import sys

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def calculate_cloud_position(cloud):
    cloud_range = []

    for r, c in cloud:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N

        cloud_range.append((nr, nc))

    return cloud_range


def rain(cloud_range):
    for r, c in cloud_range:
        arr[r][c] += 1


def water_copy_bug(cloud_range):
    for r, c in cloud_range:
        water_count = 0

        for d in range(2, 9, 2):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                water_count += 1

        arr[r][c] += water_count


def decrease_water2(cloud_range):
    initial_cloud = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in cloud_range:
                arr[i][j] -= 2
                initial_cloud.append((i, j))

    return initial_cloud


initial_cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
answer = 0

for d, s in commands:
    # 구름의 이동 후 위치 구하기
    cloud_range = calculate_cloud_position(initial_cloud)

    # 구름이 있는 곳은 물 + 1
    rain(cloud_range)

    # 물이 증가한 칸에 물 복사 버그
    water_copy_bug(cloud_range)

    # 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸에 물의 양이 2만큼 감소 + 구름 생기기
    initial_cloud = decrease_water2(cloud_range)


for i in range(N):
    answer += sum(arr[i])

print(answer)
