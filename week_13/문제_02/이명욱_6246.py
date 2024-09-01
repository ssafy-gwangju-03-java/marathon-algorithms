# r,c = 방문한 지점의 좌표, t = 목표 지점 lst의 인덱스
def dfs(r, c, t):
    global cnt
    # 목표지점의 도달했을때
    if (r, c) == q[t]:
        # 마지막 목표지점이면 cnt 증가
        if (r, c) == q[-1]:
            cnt += 1
            return
        # 중간 목표 지점이면 인덱스만 증가
        else:
            t += 1
    # 방문 쳌
    visited[r][c] = 1

    # 인접한 칸 이동
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        # 범위 내인지, 방문하지 않은 곳인지, 벽이 아닌지 확인
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and lst[nr][nc] == 0:
            # 이동한 지점에서 재귀함수 호출
            dfs(nr, nc, t)
    # 재귀함수 갔다왔을 때 방문 쳌 초기화
    visited[r][c] = 0

# 입력 받기
n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

# 목표 지점
q = []
for _ in range(m):
    a, b = map(int, input().split())
    q.append((a-1, b-1))

# 이동 가능한 경우의 수
cnt = 0
# 방문 체크
visited = [[0] * n for _ in range(n)]

# 시작 지점
sr, sc = q[0]

# 시작 지점 과 다음 목표 지점 lst 인덱스 넣어 함수 호출
dfs(sr, sc, 1)
print(cnt)
