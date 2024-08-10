import sys

N, M = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 튜플 안쓰고 리스트 써서 시간초과
cloud_list = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 구름 이동시키기
def move_cloud(cloud_list, d, s):
    new_cloud_list = []

    for cloud in cloud_list:
        r = (cloud[0] + dr[d - 1] * s) % N
        c = (cloud[1] + dc[d - 1] * s) % N
        new_cloud_list.append((r, c))

    return new_cloud_list

# 비 내리기
def rain(cloud_list, grid):
    for r, c in cloud_list:
        grid[r][c] += 1

# 물복사버그 마법
def copy_water(cloud_list, grid):
    for r, c in cloud_list:
        water_count = 0

        for d in range(1, 8, 2):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                water_count += 1

        grid[r][c] += water_count

# 새로운 구름 생성
def new_cloud(cloud_list, grid):
    new_cloud_list = []

    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and (i, j) not in cloud_list:
                grid[i][j] -= 2
                new_cloud_list.append((i, j))

    return new_cloud_list

# M번의 이동
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    cloud_list = move_cloud(cloud_list, d, s)
    rain(cloud_list, grid)
    copy_water(cloud_list, grid)
    cloud_list = new_cloud(cloud_list, grid)

print(sum(map(sum, grid)))