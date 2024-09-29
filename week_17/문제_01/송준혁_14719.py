# https://www.acmicpc.net/problem/14719

## Referenced
# https://moonsbeen.tistory.com/247

import sys

input = sys.stdin.readline

H, W = map(int, input().split())
pillars = list(map(int, input().split()))
result = 0

# 좌우 양 끝엔 물이 고이지 않음
for i in range(1, W):
    left, right = 0, 0

    # 현재 위치의 왼쪽 기둥 중 가장 높은 기둥
    for j in range(i):
        left = max(left, pillars[j])

    # 현재 위치의 오른쪽 기둥 중 가장 높은 기둥
    for j in range(i + 1, W):
        right = max(right, pillars[j])

    # 현재 위치의 높이가 양쪽 기둥보다 낮아 물이 고일 수 있다면
    if pillars[i] < left and pillars[i] < right:
        # 둘 중 낮은 기둥 기준으로 현재 위치에 고일 수 있는 물 양을 구함
        result += min(left, right) - pillars[i]

print(result)
