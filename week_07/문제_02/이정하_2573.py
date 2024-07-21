from collections import deque


def bfs(r, c):
    # 첫항처리하기, 필요한 변수 만들기
    q = deque([(r, c)])
    visited[r][c] = 1
    seaList = []

    while q:
        r, c = q.popleft()
        sea = 0  # 현재 위치의 바다 개수
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내에 있으면
            if 0 <= nr < N and 0 <= nc < M:
                if not graph[nr][nc]:  # 인접한 셀이 바다(0)인 경우
                    sea += 1  # 바다 개수 ++
                elif graph[nr][nc] and not visited[nr][nc]:  # 방문하지 않은 빙산인 경우
                    q.append((nr, nc))  # 큐에 추가하여 BFS 계속
                    visited[nr][nc] = 1  # 방문 처리
        # 빙산 주변에 바다가 있는 경우 seaList에 추가
        if sea > 0:
            seaList.append((r, c, sea))

    # 인접한 바다의 수에 따라 빙산 높이 감소
    for r, c, sea in seaList:
        graph[r][c] = max(0, graph[r][c] - sea)

    return 1  # 이 빙산 그룹 카운트하려면 1 반환


#N*M 격자
N, M = map(int, input().split())
# 초기 빙산 상태
graph = [list(map(int, input().split())) for _ in range(N)]

# 빙산 위치
ice = []
for i in range(N):
    for j in range(M):
        if graph[i][j]:  # 해당 위치에 빙산이 있는 경우
            ice.append((i, j))

# 델타배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
year = 0  # 연도

while ice:
    # 이번 해 방문 배열 초기화
    visited = [[0] * M for _ in range(N)]
    delList = []  # 이번 해에 완전히 녹을 빙산 저장
    group = 0  # 빙산 그룹 수

    for i, j in ice:
        if graph[i][j] and not visited[i][j]:  # 방문x 빙산이면
            group += bfs(i, j)  # BFS를 실행해서 그룹 카운트 ++
        if graph[i][j] == 0:  # 빙산이 녹았으면
            delList.append((i, j))  # 삭제 리스트에 추가

    if group > 1:  # 두 개 이상 빙산 그룹 있으면
        print(year)  # 빙산이 분리된 연도
        break

    # 녹은 빙산을 리스트에서 제거하고 ice 리스트 업데이트
    ice = sorted(list(set(ice) - set(delList)))
    year += 1  # 연도 ++

# 분리 x 경우 => 0
if group < 2:
    print(0)
