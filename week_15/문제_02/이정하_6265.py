from collections import deque

# 입력 받기
H, W = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
operations = [list(map(int, input().split())) for _ in range(Q)]

# 델타벡터
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c, new_color):
    # 시작 픽셀 원래 색
    before_color = image[r][c]
    # 원래꺼랑 새거랑 같으면 그냥 종료
    if before_color == new_color:
        return

    # 초기화
    queue = deque([(r, c)])

    # 탐색
    while queue:
        # pop
        cr, cc = queue.popleft()
        # 이미 뉴컬러면 패스
        if image[cr][cc] != before_color:
            continue

        # 새 색깔로
        image[cr][cc] = new_color

        # 상우하좌 탐색
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            # 다음 좌표가 범위 내 & 원래색이랑 같으면 큐에 추가
            if 0 <= nr < H and 0 <= nc < W and image[nr][nc] == before_color:
                queue.append((nr, nc))


# 연산 ㄱㄱ
for r, c, color in operations:
    bfs(r - 1, c - 1, color)  # 범위가 1부터여서 1씩 빼줌

for row in image:
    print(*row)
