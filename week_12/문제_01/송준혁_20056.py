# https://www.acmicpc.net/problem/20056

## Referenced
# https://cheon2308.tistory.com/entry/백준-20056번-파이썬-마법사-상어와-파이어볼

import sys

input = sys.stdin.readline

# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
fireballs = [list(map(int, input().split())) for _ in range(M)]

for _ in range(K):
    while fireballs:
        sr, sc, sm, ss, sd = fireballs.pop()
        # 각 파이어볼 이동
        # 0 ~ N-1 행/열 연결을 위해 N으로 나누었을 때의 나머지 값 사용
        nr = (sr - 1 + ss * dr[sd]) % N
        nc = (sc - 1 + ss * dc[sd]) % N
        # 이동한 좌표에 파이어볼 정보 저장
        grid[nr][nc].append([sm, ss, sd])

    # 좌표 탐색
    for r in range(N):
        for c in range(N):
            # 파이어볼이 2개 이상일 경우
            if len(grid[r][c]) >= 2:
                m_sum, s_sum, odds, evens, count = 0, 0, 0, 0, len(grid[r][c])
                while grid[r][c]:
                    m, s, d = grid[r][c].pop()
                    # 질량 및 속도 합 계산
                    m_sum += m
                    s_sum += s
                    # 홀/짝 방향 개수 계산
                    if d % 2 == 0:
                        evens += 1
                    else:
                        odds += 1
                # 모든 방향이 홀수 혹은 짝수일 경우
                if odds == count or evens == count:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                # 질량 합을 5로 나누었을 때 0이 아닐 경우
                if m_sum // 5:
                    # 파이어볼을 4개로 나눔
                    for i in nd:
                        fireballs.append([r, c, m_sum // 5, s_sum // count, i])

            # 파이어볼이 1개일 경우 다음번 탐색 목록에 추가
            elif len(grid[r][c]) == 1:
                fireballs.append([r, c] + grid[r][c].pop())

print(sum(i[2] for i in fireballs))
