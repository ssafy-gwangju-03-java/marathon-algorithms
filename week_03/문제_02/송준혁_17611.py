# https://www.acmicpc.net/problem/17611

## Referenced
# https://yabmoons.tistory.com/707

import sys

input = sys.stdin.readline
n = int(input())
grids = 10000001  # 최대 좌표 범위

horizontal_lines = [0] * grids  # y 좌표에서의 교차점 개수 저장 배열
vertical_lines   = [0] * grids  # x 좌표에서의 교차점 개수 저장 배열
horizontal_count = 0
vertical_count   = 0

corners = []
for _ in range(n):
    corners.append(list(map(int, input().split())))

for i in range(len(corners)):
    """
    - 두 꼭지점의 좌표를 비교하여 수평/수직 선분을 구분
    - 인덱스로 구분하기 위해 각 좌표에 500,000을 더해 인덱스로 변환
    - 구분된 선분의 시작점은 교차할 선분의 시작점이므로 교차 선분의 개수++
    - 구분된 선분의 끝점은 교차할 선분의 종료점이므로 교차 선분의 개수--
    """
    cx, cy = corners[i][0], corners[i][1]
    # (i + 1) == n일 경우 i와 0번 좌표 비교
    nx, ny = corners[(i + 1) % n][0], corners[(i + 1) % n][1]
    # x 좌표가 같음 => 수직 선분 => 수평 선분과의 교차점 개수
    if cx == nx:
        start = min(cy, ny) + 500000
        end = max(cy, ny) + 500000
        horizontal_lines[start] += 1  # 시작점이므로 교차하는 수평 선분++
        horizontal_lines[end] -= 1    # 종료점이므로 교차하는 수평 선분--
    # x 좌표가 다름 => 수평 선분 => 수직 선분과의 교차점 개수
    else:
        start = min(cx, nx) + 500000
        end = max(cx, nx) + 500000
        vertical_lines[start] += 1  # 시작점이므로 교차하는 수직 선분++
        vertical_lines[end] -= 1    # 시작점이므로 교차하는 수직 선분--

# 배열 순회하여 각 수평/수직 선분의 교차점들의 누적합 계산
# 시작점이 겹칠 경우 교차점의 누적합은 증가, 종료점이 겹칠 경우 누적합 감소
for i in range(1, grids):
    horizontal_lines[i] += horizontal_lines[i - 1]
    vertical_lines[i] += vertical_lines[i - 1]
    horizontal_count = max(horizontal_count, horizontal_lines[i])
    vertical_count = max(vertical_count, vertical_lines[i])

print(max(horizontal_count, vertical_count))


"""
# 완전탐색
corners = []
horizontal_line, vertical_line = {}, {}

for _ in range(n):
    corner = list(map(int, input().split()))
    corner[0] *= 2
    corner[1] *= 2
    corners.append(corner)

corners_x = sorted(corners, key=lambda x: (x[0], x[1]))
corners_y = sorted(corners, key=lambda x: (x[1], x[0]))
min_x, max_x = corners_x[0][0], corners_x[-1][0]
min_y, max_y = corners_y[0][1], corners_y[-1][1]

length_x = max_x + min_x + 1
length_y = max_y + min_y + 1

# 수직 선분
for x in range(len(corners_x) // 2):
    start, end = corners_x[x * 2][1], corners_x[x * 2 + 1][1]
    for i in range(start + 1, end):
        if horizontal_line.get(i):
            horizontal_line[i] += 1
        else:
            horizontal_line[i] = 1

# 수평 선분
for y in range(len(corners_y) // 2):
    start, end = corners_y[y * 2][0], corners_y[y * 2 + 1][0]
    for i in range(start + 1, end):
        if vertical_line.get(i):
            vertical_line[i] += 1
        else:
            vertical_line[i] = 1

print(max(max(horizontal_line.values()), max(vertical_line.values())))
"""
