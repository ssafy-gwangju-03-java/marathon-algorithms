# 21610 마법사 상어와 비바라기
ds = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] # 1번 이동
dd = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 4번 대각

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]  # lst[y][x] (x,y)
mv = [list(map(int, input().split())) for _ in range(m)]
cloud = [(0, n - 2), (1, n - 2), (0, n - 1), (1, n - 1)]  # x,y
new_cloud = [] # 5번 처리용 이전 구름 저장 리스트


def first(d, s):  # d방향 s칸 이동
    global cloud, new_cloud
    x, y = ds[d]
    for k in range(len(cloud)):
        i, j = cloud[k]
        mv_x = (i + (x * s)) % n
        mv_y = (j + (y * s)) % n
        cloud[k] = (mv_x, mv_y)
        new_cloud.append((mv_x, mv_y)) 


def second():  # 물 양 증가
    global lst
    for k in range(len(cloud)):
        i, j = cloud[k]
        lst[j][i] += 1


def third(): # 구름 제거
    global cloud
    cloud = []


def fourth(): # 구름 있는 칸 물복사
    for k in range(len(cloud)):
        global lst
        i, j = cloud[k]
        cnt = 0
        for p in range(4):
            dx = i + dd[p][0]
            dy = j + dd[p][1]
            if 0 <= dx < n and 0 <= dy < n: # 범위 내
                if lst[dy][dx]:
                    cnt += 1
        lst[j][i] += cnt


def fifth(): # 구름 만들기 (이전에 구름 있던 칸에는 X)
    global lst, cloud, new_cloud
    for y in range(n):
        for x in range(n):
            if (x, y) in new_cloud: # 이전 구름공간 -> 넘기기
                continue
            if lst[y][x] >= 2:
                lst[y][x] -= 2
                cloud.append((x, y))
    new_cloud.clear()


for d, s in mv:
    first(d, s)
    second()
    fourth()
    third()
    fifth()

ans = 0
for i in lst:
    ans += sum(i)
print(ans)

# 지문 3번 4번 순서 바꿔야하는게 아닌가 싶네요
