import sys

N = int(sys.stdin.readline())

# 정점을 저장할 배열
vertices = []

# 좌표를 표시해줄 x축, y축
horizontal = [0] * 1000001
vertical = [0] * 1000001

# 정점 입력
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    vertices.append((x, y))

# 선분 표시
# 입력이 시계방향으로 주어지므로 vertices의 인덱스를 따라가기
# (i + 1) % N == 맨 마지막 정점은 첫번째 정점과 이어진다
for i in range(N):
    x, y = vertices[i]
    nx, ny = vertices[(i + 1) % N]

    # x 좌표가 동일 == 수직으로 그어진 선
    if x == nx:
        s, e = min(y, ny), max(y, ny)   # 시작점, 끝점
        vertical[s + 500000] += 1       # 시작점 +1로 표시
        vertical[e + 500000] -= 1       # 끝점 -1로 표시
    # y 좌표가 동일 == 수평으로 그어진 선
    elif y == ny:
        s, e = min(x, nx), max(x, nx)
        horizontal[s + 500000] += 1
        horizontal[e + 500000] -= 1

# 누적합으로 교차되는 횟수 구하기
# 선분의 시작점이 +1, 끝점이 -1이므로 누적합을 구하면 교차 횟수를 구할 수 있음
for i in range(1, 1000001):
    horizontal[i] += horizontal[i-1]
    vertical[i] += vertical[i-1]

print(max(max(horizontal),max(vertical)))