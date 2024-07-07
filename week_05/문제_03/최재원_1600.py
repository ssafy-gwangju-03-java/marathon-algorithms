import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

horse_dr = [-2, -2, -1, 1, 2, 2, 1, -1]
horse_dc = [-1, 1, 2, 2, 1, -1, -2, -2]

K = int(input().strip())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]


def bfs():
    q = deque([(0, 0, 0)])

    visited = [[[-1] * W for _ in range(H)] for _ in range(K + 1)]
    visited[0][0][0] = 0

    while q:
        jump, r, c = q.popleft()

        # 종점에 도착하면 이동 횟수 출력 후 종료
        if r == H - 1 and c == W - 1:
            print(visited[jump][r][c])
            return

        # 4방향 움직임
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < H and 0 <= nc < W and visited[jump][nr][nc] == -1 and arr[nr][nc] == 0:
                visited[jump][nr][nc] = visited[jump][r][c] + 1
                q.append((jump, nr, nc))

        # 말처럼 움직일 수 있는 경우
        if jump < K:
            for d in range(8):
                nr = r + horse_dr[d]
                nc = c + horse_dc[d]
                if 0 <= nr < H and 0 <= nc < W and visited[jump + 1][nr][nc] == -1 and arr[nr][nc] == 0:
                    visited[jump + 1][nr][nc] = visited[jump][r][c] + 1
                    q.append((jump + 1, nr, nc))

    # 도착하지 못하면 -1 출력
    print(-1)


bfs()
