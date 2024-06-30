from collections import deque


# 블록 내려옴
def fall():
    for y in range(6):
        for x in range(10, -1, -1):  # 아래에서 위로 각 행 순회
            for fall_point in range(11, x, -1):  # 현재 위치 아래쪽에서 빈 칸 찾을 것이다
                # 현재 위치에 블록이 있고 아래 위치가 빈 칸이면
                if graph[x][y] != '.' and graph[fall_point][y] == '.':
                    graph[fall_point][y] = graph[x][y]  # 블록을 아래로 이동
                    graph[x][y] = '.'  # 현재 위치는 빈 칸으로


# 같은 색 블록 찾아서 한꺼번에 터트리기
def burst(i, j, color):
    global flag
    q = deque()
    # 시작점 처리
    q.append([i, j])
    visited[i][j] = 1
    puyo = [[i, j]]  # 같은 색 블록들 저장
    while q:  # 큐가 빌 때까지
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            # 범위내에서, 같은 색, 방문x인 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == color and not visited[nx][ny]:
                # 방문처리
                q.append([nx, ny])
                visited[nx][ny] = 1
                puyo.append([nx, ny])  # 같은 색 블록 리스트에 추가
    if len(puyo) >= 4:  # 같은 색의 블록이 4개 이상인 경우
        flag = True
        for x, y in puyo:  # 같은 색 순회
            graph[x][y] = '.'  # 그 위치를 빈 칸으로


graph = [list(input().rstrip()) for _ in range(12)]
# 델타배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            # 현재 위치에 블록이 있고 방문x 경우
            if graph[i][j] != '.' and not visited[i][j]:
                burst(i, j, graph[i][j])

    if flag:  # 블록이 터졌을 경우
        fall()  # 떨구자
        result += 1
    else:  # 더 이상 터질 블록이 없으면
        break

print(result)
