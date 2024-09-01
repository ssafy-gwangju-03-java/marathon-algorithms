from collections import deque

# bfs ? dfs? 빡구현?
# 보드의 크기 N
N = int(input())
# 사과 개수 K
K = int(input())
# 사과 위치 (r, c)
apples = [list(map(int, input().split())) for _ in range(K)]
# 뱀 방향 변환 횟수 L
L = int(input())
# 뱀 방향 변환 정보 (정수 X, 문자 C)
# 게임 시작으로부터 X 초 후 L이면 왼, D면 오. 90도 회전)
turn = [list(input().split()) for _ in range(L)]
snake = deque()
snake.append((1, 1))  # 시작 시 (1,1). 큐로 관리 ㄱㄱ
board = [[0] * (N + 1) for _ in range(N + 1)]  # 0번은 안쓰고 1~N번 칸 사용
for apple in apples:
    board[apple[0]][apple[1]] = 1  # 사과 위치 표시
sec = 0
delta = 1  # 방향 상우하좌 0123
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r, c = 1, 1
# visited = []
board[r][c] = 2  # 뱀 처음 위치 표시

# 방향 전환 횟수만큼만 돌면 안되나?
for time, C in turn:
    time = int(time)

    # 지나간 위치 좌표에 visited 1 표시하거나,
    # 지나간 위치 좌표를 전부 리스트에 넣어버리거나?
    #    그래서 한번에 for a in apples 해서 if a in 방문리스트 하면
    # 100*100 번 완탐 말고 해봐야 최대 200번만 돌만 되니까...?
    # 이렇게하면 뱀 몸통 관리 안됨
    # 매 turn 마다 현재 시간(sec) ~ 다음 방향 전환 시간(time)까지 뱀 시뮬레이션
    while sec < time:
        sec += 1
        nr, nc = r + dr[delta], c + dc[delta]  # 다음 이동할 위치

        # 벽이나 자기 몸통 부딪혔는지
        if not (1 <= nr <= N and 1 <= nc <= N) or board[nr][nc] == 2:
            print(sec)
            exit()  # 프로그램 종료

        # 안부딪혔으면 사과 여부 따라 뱀 몸통 처리
        if board[nr][nc] != 1:  # 사과 없으면
            tr, tc = snake.popleft()  # 뱀 큐에서 꼬리 삭제
            board[tr][tc] = 0  # 보드에서 뱀 꼬리 이동 처리
        else:
            board[nr][nc] = 0  # 사과 제거
        # 사과 있든없든 뱀 머리는 이동
        snake.append((nr, nc))
        board[nr][nc] = 2
        r, c = nr, nc

    # time초 후 방향 전환
    if C == 'L':
        # delta = delta - 1 if delta > 0 else delta + 3
        delta = (delta - 1) % 4  # 왼쪽 90도
    else:
        delta = (delta + 1) % 4  # 오른쪽 90도

# 혹시 방향전환 끝나고도 게임 안끝났을 수 있음
while True:
    sec += 1
    nr, nc = r + dr[delta], c + dc[delta]  # 다음 위치 계산

    # 벽이나 자기 자신과 부딪혔는지 확인
    if not (1 <= nr <= N and 1 <= nc <= N) or board[nr][nc] == 2:
        break  # 게임 종료

    if board[nr][nc] != 1:  # 다음 위치에 사과가 없으면
        tr, tc = snake.pop(0)  # 뱀의 꼬리 제거
        board[tr][tc] = 0  # 보드에서 꼬리 위치를 비움
    else:  # 다음 위치에 사과가 있으면
        board[nr][nc] = 0  # 사과 제거

    snake.append((nr, nc))  # 뱀의 새로운 머리 위치 추가
    board[nr][nc] = 2  # 보드에 새 위치 표시
    r, c = nr, nc  # 현재 위치 업데이트

print(sec)

#     nr, nc = r + dr[delta] * (time - sec), c + dc[delta] * (time - sec)
#     print(time, sec)
#     if not (1 <= nr <= N and 1 <= nc <= N):  # 범위 밖이면 리턴
#         if not 1 <= nr <= N:
#             print('nr,nc,time', nr, nc, time)
#             sec = time - (nr - N) if nr > N else time - abs(nr) - 1
#             print(sec, 'not r')
#         else:
#             sec += time - (nc - N) if nc > N else time - abs(nc) - 1
#             print(sec, 'not c')
#         break  # for문 탈출
#     # 범위 내면
#     sec = time  # 일단 게임 몇초지났는지 갱신
#     # 방문한 좌표
#     if delta % 2 == 0:  # 좌, 우면 col, 상,하면 row에 추가
#         visited.append((i, c) for i in range(r, nr + 1))
#     else:  # 좌우 col
#         visited.append((r, i) for i in range(c, nc + 1))
#
#     # time초 후 방향 전환
#     if C == 'L':
#         delta = delta - 1 if delta > 0 else delta + 3
#     else:
#         delta = delta + 1 if delta < 3 else delta - 3
#
#     # 좌표 갱신
#     r, c = nr, nc
# # for apple in apples:
# #     if apple in
#
# print(sec)
