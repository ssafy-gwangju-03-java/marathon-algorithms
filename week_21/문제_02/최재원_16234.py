import sys
from collections import deque
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(queue):
    global visited, nations, total_population
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                    visited[nr][nc] = 1
                    nations.append([nr, nc])
                    queue.append([nr, nc])
                    total_population += arr[nr][nc]

days = 0
while True:
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    opened_nations = []

    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                nations = []
                total_population = arr[r][c]
                visited[r][c] = 1
                nations.append([r, c])
                queue.append([r, c])
                bfs(queue)

                if len(nations) > 1:
                    opened_nations.append((nations, total_population))

    # 더 이상 국경이 열리지 않으면 종료
    if not opened_nations:
        break

    # 인구 이동 처리
    for nations, total_population in opened_nations:
        average_population = total_population // len(nations)
        for r, c in nations:
            arr[r][c] = average_population

    days += 1

print(days)
