import sys
sys.setrecursionlimit(10**8)

def solve(n, m, a):
    # 방문 여부
    visited = [[0] * m for _ in range(n)]
    # 안전 지대 개수
    safe_zones = 0

    dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
    dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

    def dfs(x, y, p):
        if visited[x][y] == 2:
            for i, j in p:
                visited[i][j] = 2
            return
        
        if visited[x][y] == 1:
            for i, j in p:
                visited[i][j] = 2
            return 1
        
        visited[x][y] = 1
        p.append((x, y))

        direction = a[x][y]
        nx, ny = x + dx[direction], y + dy[direction]
        return dfs(nx, ny, p)

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                safe_zones += dfs(i, j, []) or 0

    return safe_zones

n, m = map(int, input().split())
a = [input() for _ in range(n)]

print(solve(n, m, a))