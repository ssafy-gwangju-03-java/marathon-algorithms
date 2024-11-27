# https://www.acmicpc.net/problem/16933

import sys
from collections import deque

input = sys.stdin.readline


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M


def pathfinder():
    q = deque()
    q.append((0, 0, 0, 1, True))

    while q:
        # 좌표, 부순 벽 개수, 경로 개수, 낮 유무
        r, c, walls, count, day = q.popleft()

        # 목적지 도착
        if r == N - 1 and c == M - 1:
            return count

        for i in range(4):
            nr, nc = r + d[i][0], c + d[i][1]

            if is_valid(nr, nc):
                if grid[nr][nc] == 1 and walls < K and not visited[walls + 1][nr][nc]:
                    """
                    - 진행 방향이 벽
                    - 벽 개수 제한 도달 X
                    - 벽을 부쉈을 경우에 도달한 적 없는 경우
                    """
                    if day:
                        # 낮이라면 벽을 부수고 이동
                        visited[walls + 1][nr][nc] = 1
                        q.append((nr, nc, walls + 1, count + 1, not day))
                    else:
                        # 밤이라면 부수지 않고 대기
                        visited[walls][r][c] = 1
                        q.append((nr, nc, walls, count + 1, not day))
                elif grid[nr][nc] == 0 and not visited[walls][nr][nc]:
                    # 벽이 아니고 방문한 적 없는 경우, 진행
                    visited[walls][nr][nc] = 1
                    q.append((nr, nc, walls, count + 1, not day))
    return -1


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]

print(pathfinder())
