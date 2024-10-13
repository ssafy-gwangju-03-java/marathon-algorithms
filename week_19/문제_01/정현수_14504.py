from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  

# 방향: 북(0), 동(1), 남(2), 서(3)
di = [-1, 0, 1, 0]  
dj = [0, 1, 0, -1]  

def dfs(y, x, d):
    q = deque()
    q.append((y, x, d))  
    visited[y][x] = 1  

    cleaned_count = 1 

    while q:
        nowy, nowx, dir = q.popleft()
        clean = False

        # 4방향을 탐색하여 청소할 수 있는 칸을 찾음
        for _ in range(4):
            dir = (dir + 3) % 4 
            ny, nx = nowy + di[dir], nowx + dj[dir]

            # 범위 내에 있고, 청소되지 않은 빈 칸인 경우
            if 0 <= ny < n and 0 <= nx < m and lst[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append((ny, nx, dir))  
                visited[ny][nx] = 1  
                cleaned_count += 1  
                clean = True
                break  

        # 청소할 칸이 없다면 후진 시도
        if not clean:
            back_d = (dir + 2) % 4  
            by, bx = nowy + di[back_d], nowx + dj[back_d]

            if lst[by][bx] == 1:
                break
            else:
                q.append((by, bx, dir))  

    return cleaned_count

ans = dfs(r, c, d)
print(ans)
