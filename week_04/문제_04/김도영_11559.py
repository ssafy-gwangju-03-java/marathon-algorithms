# Puyo Puyo
from collections import deque

field = [list(input()) for _ in range(12)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, color):
    global pang
    q = deque()
    visited = [[0] * 6 for _ in range(12)]
    q.append((si, sj))
    visited[si][sj] = 1

    # 터트릴 위치 저장 리스트
    delete_lst = [(si, sj)]
    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 인덱스 검사
            if 0 <= ni < 12 and 0 <= nj < 6:
                # color와 field[ni][nj]가 같고, 방문하지 않았을 때
                if color == field[ni][nj] and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    delete_lst.append((ni, nj))
                    visited[ni][nj] = 1
    
    # 4개 이상이면 터트리기
    if len(delete_lst) >= 4:
        for a, b in delete_lst:
            field[a][b] = '.'
        
        return True

    return False

def move():
    for j in range(6):
        cnt = 11
        for i in range(11, -1, -1):
            if field[i][j] != ".":
                x = field[i][j]
                field[i][j] = "."
                field[cnt][j] = x
                cnt -= 1

# 연쇄 count
result = 0
while True:
    pang = False
    for i in range(12):
        for j in range(6):
            if field[i][j] == '.':
                continue

            if bfs(i, j, field[i][j]):
                pang = True

    if pang:
        move()
        result += 1
    
    else:
        break

print(result)
