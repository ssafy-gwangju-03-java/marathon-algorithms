from collections import deque

# 인접한 영역 같은 섬 번호 붙여주기
def bfs(sr, sc):
    visited[sr][sc] = land_num
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc]== 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = land_num

# 가장 짧은 다리의 길이 찾기
def bfs2(i):
    q2 = deque([])
    # 다리의 길이 기록
    distance = [[-1] * N for _ in range(N)]

    # 같은 번호의 섬일 경우 거리를 0으로
    for sr in range(N):
        for sc in range(N):
            if visited[sr][sc] == i:
                q2.append((sr, sc))
                distance[sr][sc] = 0
    while q2:
        r, c = q2.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                # 이동할 지점이 같은 섬의 번호가 아니면서 바다가 아닐때 distance 반환
                if visited[nr][nc] != i and visited[nr][nc] != 0:
                    return distance[r][c]
                # 이동할 지점이 바다이면서 방문하지 않은 곳이라면 거리 1 증가
                if visited[nr][nc] == 0 and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1
                    q2.append((nr, nc))


# 입력 받기
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 섬 번호 적을 2차원 배열
visited = [[0] * N for _ in range(N)]
# 섬 번호
land_num = 1

# 배열 순회하며
for sr in range(N):
    for sc in range(N):
        # 육지인 부부이면서 방문하지 않은(=섬 번호 안 붙여진) 육지일때 bfs 실행
        if lst[sr][sc] == 1 and visited[sr][sc] == 0:
            bfs(sr, sc)
            # 인접한 육지 체크 이후 섬 번호 1증가
            land_num += 1
# print(visited)

# 최소값 비교 변수
result = 1e9
# 섬 번호에 따라 탐색 후 최소값 설정
for i in range(1, land_num):
    result = min(result, bfs2(i))

print(result)
