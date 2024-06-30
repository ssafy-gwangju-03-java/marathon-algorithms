from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

fields = [list(input()) for _ in range(12)]
visited = [[False]* 6 for i in range(12)]


popCnt = 0

while (True) :
    isPop = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if fields[i][j] != ".":
                dq = deque()
                dq.append((i, j, fields[i][j]))
                visited[i][j] = True
                lst = []
                lst.append((i, j))
                while dq:
                    r, c, color = dq.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < 12 and  0 <= nc < 6 and not visited[nr][nc] and fields[nr][nc] == color:
                            dq.append((nr, nc, fields[nr][nc]))
                            visited[nr][nc] = True
                            lst.append((nr, nc))
                if len(lst) >= 4:
                    for k in range(len(lst)):
                        fields[lst[k][0]][lst[k][1]] = "."
                    isPop = True  
    
    for j in range(6):
        idx = 11
        for i in range(11, -1, -1):
            if fields[i][j] != ".":
                # fields[idx][j],fields[i][j] = fields[i][j], '.'
                tmp = fields[i][j]
                fields[i][j] = '.'
                fields[idx][j] = tmp
                idx -= 1

    if isPop :
        popCnt += 1
    else: break

print(popCnt)
