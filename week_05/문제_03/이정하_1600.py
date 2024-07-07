from collections import deque

# 말 이동 좌상 우상 좌하 우하 각 상하
hdr = [-1, -2, -2, -1, +1, +2, 2, 1]
hdc = [-2, -1, +1, +2, -2, -1, 1, 2]
# 인접칸 이동 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# (현재 행, 현재 열, 동작 수, 말 움직임 사용 횟수)
def bfs(start_r, start_c, K, W, H, grid):
    # 시작지점 초기화
    q1 = deque([(start_r, start_c, 0, 0)])
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    # (r,c) 위치에 말 움직임 K 번 사용햇을 때 방문 여부
    visited[start_r][start_c][0] = True

    while q1:
        r, c, steps, knight_moves_used = q1.popleft()

        # 목적지 도착하면 현재까지의 동작 수 반환
        if r == H - 1 and c == W - 1:
            return steps

        # 일반 이동
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 범위 내에서,방문 x, 장애물 x
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][knight_moves_used] and grid[nr][nc] == 0:
                visited[nr][nc][knight_moves_used] = True
                q1.append((nr, nc, steps + 1, knight_moves_used))

        # 횟수 남아있으면
        if knight_moves_used < K:
            for d in range(8):
                # 말처럼 움직임
                nr, nc = r + hdr[d], c + hdc[d]
                # 범위 내에서, 방문x, 장애물 x
                if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][knight_moves_used + 1] and grid[nr][nc] == 0:
                    visited[nr][nc][knight_moves_used + 1] = True
                    q1.append((nr, nc, steps + 1, knight_moves_used + 1))
    # 여기까지 왔으면 -1
    return -1


# 원숭이가 말처럼 움직일 수 있는 횟수 K번
K = int(input())
# H*W 격자
W, H = map(int, input().split())
# 격자판 - 0 평지, 1 장애물
grid = [list(map(int, input().split())) for _ in range(H)]

# (0, 0)에서 시작, 말의 움직임 0번
result = bfs(0, 0, K, W, H, grid)
print(result)
