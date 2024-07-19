from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    vis[y][x] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not vis[ny][nx] and arr[ny][nx]:
                    vis[ny][nx] = 1
                    q.append((nx, ny))


n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    bing = 0  # 빙산 개수
    arr = [x[:] for x in lst]  # 현재 리스트 복사
    vis = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if not lst[ny][nx]:  # 주변이 바다면
                            arr[i][j] -= 1  # 깎기
                            if arr[i][j] == 0:  # 0되면 탈출
                                break
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not vis[i][j]:  # 얼음은 있고 방문하지 않은 빙산의 경우
                bfs(j, i)  # bfs로 연결된 얼음 다 방문처리
                bing += 1  # 빙산+1
    chk = 0  # 상태 변수
    ans += 1  # 녹은 횟수 추가
    lst = [x[:] for x in arr]  # 1회 녹은 상태 업데이트
    if bing == 0:  # 2회가 되는 경우 없이 바로 다 녹은경우 chk=0으로 그대로 넘김
        break
    if bing >= 2:  # 2개 이상 되는 경우
        chk = 1  # 변수 업데이트
        break
if chk:  # 2회이상 되는 경우가 있을 때
    print(ans)
else:
    print(0)
