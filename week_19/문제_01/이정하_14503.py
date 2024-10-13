# 1. 입력
# 2. DFS: 로청 움직임
#    a. 현재 위치 청소
#    b. 주변 4칸 확인
#       - 청소되지 않은 빈 칸이 있는 경우: 그 방향으로 회전하고 한 칸 전진 후 청소
#       - 청소되지 않은 빈 칸이 없는 경우:
#         * 뒤쪽 칸이 벽이 아니라면 후진
#         * 뒤쪽 칸이 벽이라면 작동 중지
#    c. 반복

# 방 크기 N*M
N, M = map(int, input().split())
# 로청 시작 좌표(r,c), 처음 방향 d (0123 북동남서)
r, c, d = map(int, input().split())
# N줄 각 장소 상태 M개씩 - 0 청소x빈칸, 1 벽
state = [list(map(int, input().split())) for _ in range(N)]

# 델타배열 0123 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 1  # 청소한 칸 개수/ 최초 시작하는 칸


def dfs(r, c, depth):
    global ans, d
    if depth == 4:  # 네 방향 모두 탐색했으면
        # 후진 가능 여부 확인
        nr = r + dr[(d - 2) % 4]  # 현재 방향의 반대 방향으로
        nc = c + dc[(d - 2) % 4]
        if state[nr][nc] == 2:  # 후진할 수 있는 경우 (이미 청소한 칸)
            dfs(nr, nc, 0)
        else:  # 후진할 수 없는 경우 (벽이거나 범위 밖)
            print(ans)
            exit(0)
    # 왼쪽 방향으로 회전
    nr = r + dr[(d - 1) % 4]
    nc = c + dc[(d - 1) % 4]

    if state[nr][nc] == 0:  # 왼쪽 방향이 청소되지 않은 빈 칸이면
        state[nr][nc] = 2  # 청소햇음 표시
        ans += 1
        d = (d - 1) % 4  # 방향 갱신
        dfs(nr, nc, 0)  # 그 칸 가서 다시 탐색 시작

    elif state[nr][nc] == 1 or state[nr][nc] == 2:  # 왼쪽 방향이 벽이거나 이미 청소했으면
        d = (d - 1) % 4  # 방향만 회전
        dfs(r, c, depth + 1)  # 현재 위치에서 다음 방향 탐색


# 시작점 청소
state[r][c] = 2
dfs(r, c, 0)
