# 뿌요뿌요

from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
field_info = []

# 필드 정보 입력 받기
for _ in range(12):
    field_info.append(list(input()))

# 뿌요 4개 이상인지 확인
def bfs(a, b, c):
    global boom_flag
    boom_list = []
    boom_list.append([a, b])
    deq = deque()
    deq.append([a, b])
    field_check[a][b] = 1
    # 인접한 같은색의 개수
    n = 1
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                # 같은 색인지, 방문하지 않은 장소인지
                if field_info[nx][ny] == c and not field_check[nx][ny]:
                    field_check[nx][ny] = 1
                    deq.append([nx, ny])
                    boom_list.append([nx, ny])
                    n += 1
    # 4개 이상이면 터트리기
    if n >= 4:
        for b in boom_list:
            field_info[b[0]][b[1]] = '.'
        boom_flag = 1

# 뿌요 터트린 개수
boom_count = 0
while True:
    boom_flag = 0
    field_check = [[0] * 6 for _ in range(12)]
    # 빈칸이 아니면 bfs 탐색
    for i in range(12):
        for j in range(6):
            if field_info[i][j] != '.':
                bfs(i, j, field_info[i][j])
    # 빈칸으로 떨어트리기
    for i in range(6):
        rotate_queue = deque()
        # 밑에서부터 순회
        for j in range(11, -1, -1):
            if field_info[j][i] != '.':
                rotate_queue.append(field_info[j][i])
        for j in range(11, -1, -1):
            if rotate_queue:
                field_info[j][i] = rotate_queue.popleft()
            else:
                field_info[j][i] = '.'
    # 뿌요 터지면 boom_count 1 증가
    if not boom_flag:
        break
    else:
        boom_count += 1

print(boom_count)