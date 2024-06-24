from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    vis[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= 0 or nx > n or ny <= 0 or ny > n:
                continue
            if [ny, nx] in lst[y][x]: # 도로를 지나가야하면 패스
                continue
            if vis[ny][nx]: # 이미 방문했으면 패스
                continue
            q.append((ny, nx))
            vis[ny][nx] = 1


n, k, r = map(int, input().split())
lst = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split()) # (r1,c1) , (r2,c2)가 도로로 연결된 것을 표시
    lst[r1][c1].append([r2, c2])
    lst[r2][c2].append([r1, c1])

cow = [list(map(int, input().split())) for _ in range(k)]
vis = [[0] * (n + 1) for _ in range(n + 1)]
cnt = 0

for i in cow: # 각각의 소들을 전부 bfs 돌림
    vis = [[0] * (n + 1) for _ in range(n + 1)]
    y = i[0]
    x = i[1]
    bfs(y, x)
    for j in cow:
        if not vis[j[0]][j[1]]: # 첫 for문의 소가 못만난 소가 있다면 cnt+=1
            cnt += 1
print(cnt // 2) # ex) 1번과 2번이 길을 건너야 만날 수 있을 때 -> 1번->2번 cnt+=1 / 2번->1번 cnt+=1이므로 반으로 나눠주면 정답
