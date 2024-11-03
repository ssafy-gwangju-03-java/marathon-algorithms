# 21609 상어 중학교

from collections import deque


def find_groups(board, N):  # 블록 그룹들을 찾기
    visited = [[False] * N for _ in range(N)]
    largest_group = []  # 가장 큰 블록 그룹
    max_rainbow = -1  # 최대 무지개 블록 수
    max_standard = (-1, -1)  # 기준 블록 좌표

    def bfs(x, y, color):  # BFS
        rainbow = []  # 무지개 블록
        blocks = [(x, y)]  # 일반 블록
        Q = deque([(x, y)])
        temp = {(x, y)}  # 현재 탐색에서의 방문 여부

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while Q:
            cx, cy = Q.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if (nx, ny) in temp:
                    continue

                if board[nx][ny] == color or board[nx][ny] == 0:
                    if board[nx][ny] == 0:
                        rainbow.append((nx, ny))
                    else:
                        blocks.append((nx, ny))
                    Q.append((nx, ny))
                    temp.add((nx, ny))

        return blocks, rainbow

    # 모든 칸에 대해 블록 그룹 찾기
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                blocks, rainbow = bfs(i, j, board[i][j])

                # 블록 그룹 조건: 일반 블록 1개 이상, 총 블록 2개 이상
                if len(blocks) + len(rainbow) >= 2:
                    # 기준 블록 찾기 (일반 블록 중 행,열이 가장 작은 블록)
                    standard = min((x, y) for x, y in blocks)

                    # 현재 그룹과 최대 그룹 비교
                    if (len(blocks) + len(rainbow), len(rainbow), standard) > (
                            len(largest_group), max_rainbow, max_standard):
                        largest_group = blocks + rainbow
                        max_rainbow = len(rainbow)
                        max_standard = standard

                # 일반 블록만 방문 체크
                for block in blocks:
                    visited[block[0]][block[1]] = True

    return largest_group


def remove(board, blocks):  # 블록 제거하고 점수 반환
    if not blocks:  # 블록이 없으면 0점
        return 0

    score = len(blocks) ** 2  # 점수는 블록 수의 제곱
    for x, y in blocks:
        board[x][y] = -2  # 빈칸 : -2
    return score


def drop(board, N):  # 중력 작용 - 블록들을 아래로 떨어뜨림
    for j in range(N):
        empty = N - 1  # 가장 아래부터 시작
        for i in range(N - 1, -1, -1):
            if board[i][j] == -1:  # 검은 블록이면
                empty = i - 1  # 그 위부터 다시 시작
            elif board[i][j] >= 0:  # 일반 블록이나 무지개 블록이면
                if empty != i:  # 현재 위치가 아니면
                    board[empty][j] = board[i][j]
                    board[i][j] = -2
                empty -= 1


def rotate(board, N):  # 반시계 방향 90도 회전
    new_board = [[-2] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - 1 - j][i] = board[i][j]

    for i in range(N):
        for j in range(N):
            board[i][j] = new_board[i][j]


def solve(n, m, board):
    score = 0

    while True:
        blocks = find_groups(board, n)
        if not blocks:  # 더 이상 그룹이 없으면 종료
            break

        score += remove(board, blocks)
        drop(board, n)  # 중력
        rotate(board, n)  # 90도 반시계 회전
        drop(board, n)  # 다시 중력

    return score


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, board))