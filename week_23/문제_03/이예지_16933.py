# 16933 벽 부수고 이동하기 3
# 시간초과 슬프다ㅠㅠㅠ
# https://ku-hug.tistory.com/156

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    ans = 1  # 이동 거리
    time = True  # True: 낮, False: 밤

    while q:
        # 현재 큐에 있는 모든 위치를 처리 (같은 시간대의 이동을 한번에 처리)
        for _ in range(len(q)):
            i, j, w = q.popleft()  # 현재 위치와 부순 벽의 개수

            if i == n - 1 and j == m - 1:  # 도착
                print(ans)
                return

            for dy, dx in dir:
                ni, nj = i + dy, j + dx

                # 범위 체크 및 더 적은 벽을 부수고 방문한 경우가 있는지 체크
                if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] <= w:
                    continue

                # 1. 빈 공간인 경우 - 낮/밤 관계없이 이동 가능
                if graph[ni][nj] == '0':
                    q.append((ni, nj, w))
                    visited[ni][nj] = w

                # 2. 벽인 경우 - 벽을 더 부술 수 있을 때만
                elif w < k:
                    if not time:  # 밤이면 현재 위치에서 대기
                        q.append((i, j, w))
                    else:  # 낮이면 벽 부수고 이동
                        visited[ni][nj] = w
                        q.append((ni, nj, w + 1))

        ans += 1
        time = not time  # 낮/밤 전환

    print(-1)
    return


n, m, k = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]  # 방문 배열은 부순 벽의 개수만 저장
visited[0][0] = 0
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
bfs((0, 0, 0))




# 원래 내 풀이
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def bfs(n, m, k, maps):
#     move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     # visited[x][y][벽 부순 횟수(k)][낮/밤] = 최단 거리 -> 4차원?
#     visited = [[[[False]*2 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
#
#     # 시작점 초기화
#     Q = deque([(0, 0, 0, 0, 1)])
#     visited[0][0][0][0] = True
#
#     while Q:
#         x, y, wall, day, dist = Q.popleft()
#
#         # 목적지 도달
#         if x == n-1 and y == m-1:
#             return dist
#
#         # 상하좌우 이동
#         for dx, dy in move:
#             nx = x + dx
#             ny = y + dy
#
#             if not (0 <= nx < n and 0 <= ny < m):
#                 continue
#
#             # 1. 빈 공간 이동
#             if maps[nx][ny] == '0' and not visited[nx][ny][wall][1-day]:
#                 visited[nx][ny][wall][1-day] = True
#                 Q.append((nx, ny, wall, 1-day, dist+1))
#
#             # 2. 벽을 만난 경우
#             elif maps[nx][ny] == '1' and wall < k:
#             # 2-1. 낮 : 벽 부수고 이동 가능
#                 if day == 0 and not visited[nx][ny][wall+1][1-day]:
#                     visited[nx][ny][wall+1][1-day] = True
#                     Q.append((nx, ny, wall+1, 1-day, dist+1))
#             # 2-2. 밤 : 벽 부수기X, 이동X --> 오히려 기다리는 게 상책
#                 elif day == 1 and not visited[x][y][wall][1-day]:
#                     visited[x][y][wall][1-day] = True
#                     Q.append((x, y, wall, 1-day, dist+1))
#     return -1
#
# n, m, k = map(int, input().split())
# maps = [list(input().strip()) for _ in range(n)]
# print(bfs(n, m, k, maps))