import sys
sys.setrecursionlimit(10**6)

# 0-북, 1-동, 2-남, 3-서
dr_dc = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(sr, sc, d):
    global cnt
    # 현재 위치를 청소
    if lst[sr][sc] == 0 and visited[sr][sc] == 0:
        cnt += 1
        visited[sr][sc] = 1

    # 4방향 확인 (반시계 방향으로 회전하면서 탐색)
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향으로 회전
        nr, nc = sr + dr_dc[d][0], sc + dr_dc[d][1]

        # 청소하지 않은 곳이 있다면 이동
        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0 and visited[nr][nc] == 0:
            dfs(nr, nc, d)
            return  # 이동 후 바로 재귀를 끝냄

    # 4방향 모두 청소되었거나 벽인 경우 후진
    back_d = (d + 2) % 4  # 반대 방향
    back_r, back_c = sr + dr_dc[back_d][0], sc + dr_dc[back_d][1]

    # 후진할 수 있으면 후진
    if 0 <= back_r < N and 0 <= back_c < M and lst[back_r][back_c] != 1:
        dfs(back_r, back_c, d)  # 후진한 위치에서 다시 탐색
    else:
        return  # 후진도 못하면 종료


N, M = map(int, input().split())
sr, sc, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# print(sr, sc, d)
# print(lst)

cnt = 0
dfs(sr, sc, d)
print(cnt)