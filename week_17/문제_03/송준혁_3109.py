# https://www.acmicpc.net/problem/3109

## Referenced
# https://wiselog.tistory.com/140

import sys

input = sys.stdin.readline


def check(r, c):
    # 현재 위치 방문 처리
    # 한 번 탐색된 경로는 다시 방문하지 않음
    pipe_map[r][c] = "*"

    # 오른쪽 마지막 열 도달: 파이프 완성
    if c == C - 1:
        return True

    # 오른쪽 위 좌표에 설치 할 수 있다면 재귀 진입
    if r > 0 and pipe_map[r - 1][c + 1] == ".":
        if check(r - 1, c + 1):
            return True
    # 오른쪽 좌표에 설치 할 수 있다면 재귀 진입
    if pipe_map[r][c + 1] == ".":
        if check(r, c + 1):
            return True
    # 오른쪽 아래 좌표에 설치 할 수 있다면 재귀 진입
    if r + 1 < R and pipe_map[r + 1][c + 1] == ".":
        if check(r + 1, c + 1):
            return True
    return False


R, C = map(int, input().split())
pipe_map = [list(input().strip()) for _ in range(R)]
result = 0

# 맨 위 행부터 마지막 행까지 첫 열에서 탐색 시작
for i in range(R):
    if check(i, 0):
        result += 1

print(result)
