from collections import deque
import sys

input = sys.stdin.readline

# 격자의 크기 입력 (n: 세로, m: 가로)
n, m = map(int, input().split())
# 치즈 정보 입력 (0: 빈 공간, 1: 치즈)
board = [list(map(int, input().split())) for _ in range(n)]
# 방문 여부를 체크하는 배열
visit = [[False] * m for _ in range(n)]
# 상하좌우 이동을 위한 방향 벡터
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 초기 치즈의 크기 계산
# 가장자리는 항상 비어있으므로 1~n-2, 1~m-2 범위만 확인
cheese_size = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j]:
            cheese_size += 1

# 시간 카운터
t = 0
while True:
    t += 1
    # BFS를 위한 큐 초기화 (0,0)부터 시작 (외부 공기)
    q = deque([(0, 0)])
    # 매 시간마다 새로운 방문 배열 생성
    visit_tmp = [i[:] for i in visit]
    # 이번에 녹을 치즈의 위치를 저장할 set
    melt = set()

    # BFS로 외부 공기와 접촉한 치즈 찾기
    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for a, b in move:
            dx = x + a;
            dy = y + b
            # 격자 범위 내이고 아직 방문하지 않은 위치인 경우
            if n > dx >= 0 and m > dy >= 0 and not visit_tmp[dx][dy]:
                visit_tmp[dx][dy] = True
                # 빈 공간인 경우 큐에 추가
                if board[dx][dy] == 0:
                    q.append((dx, dy))
                # 치즈인 경우 녹을 위치에 추가
                else:
                    melt.add((dx, dy))

    # 모든 치즈가 녹았는지 확인
    if cheese_size - len(melt) == 0:
        break
    # 아직 치즈가 남아있으면 크기 갱신
    else:
        cheese_size -= len(melt)

    # 이번에 녹을 치즈들을 모두 녹임 (0으로 변경)
    for x, y in melt:
        board[x][y] = 0

# t: 모든 치즈가 녹는데 걸린 시간
# cheese_size: 마지막으로 녹기 직전에 남아있던 치즈 크기
print(t, cheese_size, sep="\n")