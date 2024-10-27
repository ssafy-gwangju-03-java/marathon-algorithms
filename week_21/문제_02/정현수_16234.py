from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    union = [(x, y)]
    total_population = A[x][y]
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[cx][cy] - A[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += A[nx][ny]

    if len(union) > 1:
        new_population = total_population // len(union)
        for ux, uy in union:
            A[ux][uy] = new_population
        return True
    return False

days = 0
while 1:
    visited = [[False] * N for _ in range(N)]
    is_population_moved = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    is_population_moved = True

    if not is_population_moved:
        break
    
    days += 1

print(days)
