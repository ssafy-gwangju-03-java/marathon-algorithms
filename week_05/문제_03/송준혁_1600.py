# https://www.acmicpc.net/problem/1600

## Referenced
# https://www.acmicpc.net/board/view/117327
# https://www.acmicpc.net/board/view/141358

import sys
from collections import deque

input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
knight = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def bfs(r, c):
    def is_valid(r, c):
        return 0 <= r < H and 0 <= c < W

    def has_reached(r, c):
        return r == H - 1 and c == W - 1

    q = deque()
    # 덱에 누적 나이트 방식 이동 횟수도 같이 저장
    q.append((0, r, c))
    # 나이트 방식으로 이동한 횟수를 인덱스로 하는 다차원 배열 생성
    # visited[move][r][c]: (r, c)에 도달했을 때 사용한 나이트 방식 이동 횟수 = move
    visited = [[[0] * W for _ in range(H)] for _ in range(K + 1)]

    while q:
        move, sr, sc = q.popleft()

        for i in range(4):
            nr, nc = sr + d[i][0], sc + d[i][1]
            if is_valid(nr, nc) and grid[nr][nc] != 1 and not visited[move][nr][nc]:
                if has_reached(nr, nc):
                    return visited[move][sr][sc] + 1
                visited[move][nr][nc] = visited[move][sr][sc] + 1
                q.append((move, nr, nc))

        # 나이트 이동 횟수 제한에 도달하지 않았다면 나이트 방식으로도 이동 가능
        if move < K:
            for i in range(len(knight)):
                nr, nc = sr + knight[i][0], sc + knight[i][1]
                # 나이트 방식 이동 시 횟수++ 이므로 방문 기록은 [move + 1]에 해야함
                if is_valid(nr, nc) and grid[nr][nc] != 1 and not visited[move + 1][nr][nc]:
                    if has_reached(nr, nc):
                        # 다음 이동 좌표가 목표 좌표일 경우, 이동 직전의 거리가 필요하기 때문에
                        # [move + 1]이 아닌 [move]를 인덱스로 사용
                        return visited[move][sr][sc] + 1
                    visited[move + 1][nr][nc] = visited[move][sr][sc] + 1
                    q.append((move + 1, nr, nc))

    # 도달 불가
    return -1


# 최소 크기 예외 처리
# https://www.acmicpc.net/board/view/115331
if W * H == 1:
    print(0)
else:
    print(bfs(0, 0))
