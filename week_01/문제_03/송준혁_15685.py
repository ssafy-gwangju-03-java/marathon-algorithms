# https://www.acmicpc.net/problem/15685

import sys

input = sys.stdin.readline


def dragon_generator(sc, sr, d_list, target_gen, current_gen):
    """
    d_list: 드래곤 커브의 진행 방향을 저장할 배열
    target_gen: 목표 세대
    current_gen: 현재 세대

    90도 시계방향 회전시 진행방향 변화
    0 -> 1
    1 -> 2
    2 -> 3
    3 -> 0
    """

    graph[sr][sc] = 1

    # 시작점에서 이전 세대 드래곤 커브를 역으로 그려나가기 위해 역배열 사용
    d_reversed = list(reversed(d_list))
    # 이전 세대 드래곤 커브의 진행 방향 순회
    for d in d_reversed:
        # 0세대 이후일 경우만 90도 회전 후 방향 배열에 저장
        if current_gen > 0:
            d = d + 1 if d < 3 else 0
            d_list.append(d)

        nr, nc = sr + dr[d], sc + dc[d]
        graph[nr][nc] = 1
        sr, sc = nr, nc

    # 0세대 커브이거나 목표 세대에 도달 시 재귀 종료
    if target_gen == 0 or target_gen == current_gen:
        return

    dragon_generator(nc, nr, d_list, target_gen, current_gen + 1)


N = int(input())

graph = [[0] * 101 for _ in range(101)]

# 우 상 좌 하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for i in range(N):
    sc, sr, d, g = map(int, input().split())
    dragon_generator(sr, sc, [d], g, 0)

# 우->상->좌->하 순서로 꼭지점을 검사
# x 좌표는 0~99, y 좌표는 1~100
squares = 0
for r in range(1, 101):
    for c in range(100):
        if graph[r][c]:
            sr, sc, count = r, c, 0
            for d in range(4):
                nr, nc = sr + dr[d], sc + dc[d]
                if graph[nr][nc]:
                    count += 1
                    sr, sc = nr, nc
                else:
                    break

            if count == 4:
                squares += 1

print(squares)
