# 완탐으로 풀면 시간초과(범위가 백만*백만)
# 누적합으로 ㄱㄱ

# N: 꼭지점 개수
N = int(input())
# vertex: 꼭지점좌표(x,y) N개
vertex = [list(map(int, input().split())) for _ in range(N)]

# 다각형 그린 좌표형면
polygon = []
for x, y in vertex:
    x += 500000
    y += 500000
    polygon.append((x, y))

# 다각형 좌표 쌍을 순회하면서
# x좌표 같으면 수직
# y 좌표 같으면 수평
# 수평선 H, 수직선 V
cnt_H = [0] * 1000001
cnt_V = [0] * 1000001
for i in range(N):
    x, y = polygon[i]
    nx, ny = polygon[(i + 1) % N]  # 맨 마지막꺼는 맨 처음꺼가 다음이라서

    # x 좌표 같으면 수직선임
    if x == nx:
        if y > ny:
            max_y = y
            min_y = ny
        else:
            max_y = ny
            min_y = y
        cnt_V[min_y] += 1
        cnt_V[max_y] -= 1
    # y좌표 같으면 수평선
    else:
        if x > nx:
            max_x = x
            min_x = nx
        else:
            max_x = nx
            min_x = x
        cnt_H[min_x] += 1
        cnt_H[max_x] -= 1

# 누적합 구하기
for i in range(1, 1000001):
    cnt_H[i] += cnt_H[i - 1]
    cnt_V[i] += cnt_V[i - 1]
# 최댓값
ans = 0
for i in range(1, 1000001):
    ans = max(max(cnt_H[i], cnt_V[i]), ans)

print(ans)