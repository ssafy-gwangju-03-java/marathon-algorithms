# 6246 순서대로 방문하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
vis_list = []
for _ in range(m):
    y, x = map(int, input().split())
    vis_list.append((y - 1, x - 1))
cnt = 0


def dfs(now, next):
    global cnt
    if now == vis_list[next]: # 다음 목적지 도착 
        if next == len(vis_list) - 1: # 최종 목적지면 cnt+=1
            cnt += 1
            return
        else: # 중간 목적지면 다음 목적지로 idx+=1
            next += 1
    y, x = now
    vis[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not vis[ny][nx] and not lst[ny][nx]:
            dfs((ny, nx), next)
    vis[y][x] = 0


dfs(vis_list[0], 1)  # 목적지와 다음 목적지 인덱스
print(cnt)
