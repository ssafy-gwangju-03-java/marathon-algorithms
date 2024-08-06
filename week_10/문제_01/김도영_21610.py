# 마법사 상어와 비바라기

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

move_lst = [list(map(int, input().split())) for _ in range(M)]

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름 위치
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

def move_cloud(cloud, d, s):
    new_cloud = []
    for i, j in cloud:
        ni = (i + di[d] * s) % N
        nj = (j + dj[d] * s) % N
        new_cloud.append((ni, nj))
    
    return new_cloud

# 비 내림 
def rain(cloud):
    for i, j in cloud:
        arr[i][j] += 1

# 물 복사 버그
def water(cloud):
    for i, j in cloud:
        count = 0
        for d in range(1, 8, 2):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                count += 1
        
        arr[i][j] += count

# 새로운 구름 생성
def create_cloud(last_cloud):
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in last_cloud:
                new_cloud.append((i, j))
                arr[i][j] -= 2

    return new_cloud

for x, y in move_lst:
    x -= 1
    cloud = move_cloud(cloud, x, y)
    rain(cloud)
    water(cloud)
    last_cloud = cloud
    cloud = create_cloud(last_cloud)

result = sum(map(sum, arr))
print(result)