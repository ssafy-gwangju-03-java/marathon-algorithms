# 6274 안전운전을 도와줄 차세대 지능형 교통시스템
n, t = map(int, input().split())
lst = [[0] * n for _ in range(n)]
vis = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        lst[i][j] = list(map(int, input().split()))

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
u = dir[0]
d = dir[1]
l = dir[2]
r = dir[3]
direction = {
    (1, 0): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (0, -1): 3,
}  # 다음 진행방향 넘겨주기 위함
road = {  # 길 데이터 저장
    1: [u, r, d],
    2: [l, u, r],
    3: [d, l, u],
    4: [r, d, l],
    5: [u, r],
    6: [l, u],
    7: [d, l],
    8: [r, d],
    9: [r, d],
    10: [u, r],
    11: [l, u],
    12: [d, l],
}


def drive(T, y, x, direc):
    vis[y][x] = 1  # 방문 처리
    if T == t:  # 시간 끝
        return
    sign = lst[y][x]
    if sign[T % 4] % 4 == direc:  # 진행 방향이 신호와 일치해야 진행가능
        for dy, dx in road[sign[T % 4]]:
            r = y + dy
            c = x + dx
            if 0 <= r < n and 0 <= c < n:
                drive(T + 1, r, c, direction[(dy, dx)])


drive(0, 0, 0, 2)  # 0초 0,0 방향 위(2)
ans = 0
for i in vis:
    ans += sum(i)
print(ans)
