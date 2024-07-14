from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def island(y, x, cnt):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        vis[y][x] = cnt # 섬 번호
        chk = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if lst[ny][nx] and not vis[ny][nx]: # 이어져 있고 방문 안했으면 q에 append
                    q.append((ny, nx))
                    vis[ny][nx] = cnt
                if not lst[ny][nx] and not chk: # 범위 내에 옆에 0이 있고 아직 append를 안한 상태(chk=0)
                    checklist[cnt].append((y, x)) # 경계점 리스트에 append
                    chk = 1 # 중복해서 들어가는 것 방지용


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
checklist = [[] for _ in range(n * n // 2 + 1)]
# logic
# 섬 구분하면서 경계선만 뽑아서 넣기
# -> checklist 2차원 배열에서 섬 번호에 맞춰서 append
# -> 경계구분은 상하좌우에 0이 하나라도 있으면 경계로 처리
cnt = 1
for y in range(n):
    for x in range(n):
        if lst[y][x] and not vis[y][x]:
            island(y, x, cnt)
            cnt += 1
ans = n * n # 최대값 설정
for i in range(1, cnt - 1):
    for j in range(i + 1, cnt):
        for a in checklist[i]:
            y, x = a
            for b in checklist[j]:
                yy, xx = b
                ans = min(ans, abs(y - yy) + abs(x - xx) - 1) # 다른 섬의 모든 경계점 사이 거리를 구해서 반영

print(ans)
