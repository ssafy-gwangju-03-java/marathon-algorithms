# 델타배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 섬 찾기
# (시작좌표), 섬 개수(번호)
def bfs_island(sr, sc, no):
    # 1. 필요한 변수 만들기
    queue = []

    # 2. 첫항처리하기
    visited[sr][sc] = 1
    queue.append((sr, sc))
    island[sr][sc] = no  # 섬에다 섬 번호 붙여주기

    # 3. 탐색
    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위내에 있고, 섬인데, 방문x
            if 0 <= nr < N and 0 <= nc < N and island[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc))
                island[nr][nc] = no


# 가장 짧은 다리 길이 찾기
def bfs_bridge(n):  # 섬 번호 받아오기
    global ans
    # 1. 필요한 변수만들기
    distance = [[-1] * N for _ in range(N)]
    queue = []

    # 2.첫항 처리하기 - n번 섬에 속하는 좌표 모두 큐에 삽입, 거리는 0
    for i in range(N):
        for j in range(N):
            if island[i][j] == n:  # 이번 차례의 섬 번호이면
                queue.append((i, j))
                distance[i][j] = 0
    # 3. 탐색
    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 못가는 곳이면 continue
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue  # 헉 설마 - 그래도 안됨ㅜ
            # 다른 섬 만났을 때 최솟값이면 저장
            if island[nr][nc] > 0 and island[nr][nc] != n:
                ans = min(ans, distance[r][c])
                return
            # 바다 만났는데 아직 방문 안했으면? 길이 ++, 큐에 위치 삽입
            if island[nr][nc] == 0 and distance[nr][nc] == -1:
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))


# 지도 크기 N (<= 100 )
N = int(input())
# N*N 지도 0:바다 / 1:육지
island = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 1  # 섬 개수(번호)
ans = N * N  # 가장 짧은 다리 길이

# 섬 찾기
for r in range(N):
    for c in range(N):
        # 방문 안했고 섬 있으면
        if island[r][c] == 1 and not visited[r][c]:
            bfs_island(r, c, cnt)  # 탐색 시작 지점은 r,c!!!
            # bfs_island(r, c)
            cnt += 1  # 섬 개수(번호) ++

# 가장 짧은 다리 하나의 길이 찾기
for i in range(1, cnt):
    bfs_bridge(i)

print(ans)
