# https://softeer.ai/practice/6246

## Referenced
# https://baebalja.tistory.com/618


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def pathfinder(sr, sc, target, result):
    # 최종 목표 지점에 도착했을 경우 가능 경로의 수 ++
    if target == M + 1:
        return result + 1

    for i in range(4):
        nr, nc = sr + d[i][0], sc + d[i][1]
        # 다음 좌표가 맵 내에 있고, 방문한 적 없고, 벽이 아니라면
        if is_valid(nr, nc) and not visited[nr][nc] and grid[nr][nc] != 1:
            # 다음 좌표가 다음 방문 순서라면
            if grid[nr][nc] == target:
                # 방문 처리 후 다음 목적지로 이동
                visited[nr][nc] = 1
                result = pathfinder(nr, nc, target + 1, result)
            # 방문 순서가 아닐 경우
            else:
                # 방문 처리 후 기존 목적지 탐색
                visited[nr][nc] = 1
                result = pathfinder(nr, nc, target, result)

            # 방문 처리 취소 후 나머지 방향 탐색
            visited[nr][nc] = 0

    return result


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
sr, sc, idx = 0, 0, 2

# 최초 좌표를 출발시 설정 후 방문 처리
# 이후 입력되는 좌표의 순서를 증가시켜 맵 내 목표로 설정
for i in range(M):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if i == 0:
        sr, sc = r, c
        visited[sr][sc] = 1
    else:
        grid[r][c] = idx
        idx += 1

print(pathfinder(sr, sc, 2, 0))
