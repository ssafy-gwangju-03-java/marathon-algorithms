# N행 M열 영역
N, M = map(int, input().split())
# 지도 정보 입력 받기
area = [list(input()) for _ in range(N)]

# 델타배열 딕셔너리로 => 문자로 들어오는 방향 때문에
dr = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dc = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

visited = [[0] * M for _ in range(N)]
# 세이프존 개수
safe_zone_count = 0


def dfs(r, c):
    stack = [(r, c)]
    path = set()  # 현재 탐색 중인 경로 저장
    while stack:
        cr, cc = stack.pop()
        # 이미 방문한 지점이면 무시
        if visited[cr][cc]:
            continue
        # 현재 지점 방문 처리 후 경로에 추가
        visited[cr][cc] = 1
        path.add((cr, cc))
        # 현재 지점에서 이동할 다음 지점 계산
        nr = cr + dr[area[cr][cc]]
        nc = cc + dc[area[cr][cc]]
        # 다음 지점이 현재 경로에 있다는 것 => 사이클 존재
        if (nr, nc) in path:
            return 1  # 사이클 존재함
        # 다음 지점을 아직 방문 안했으면 스택에 추가
        if not visited[nr][nc]:
            stack.append((nr, nc))
    return 0  # 사이클 없음


# 모든 지점을 탐색=> 세이프존 개수
for i in range(N):
    for j in range(M):
        # 아직 방문x 지점에 대해 DFS 탐색
        if not visited[i][j]:
            # DFS로 사이클이 발견=> 세이프존 개수 증가
            if dfs(i, j):
                safe_zone_count += 1

print(safe_zone_count)
