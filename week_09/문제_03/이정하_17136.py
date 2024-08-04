from itertools import product
board = [list(map(int, input().split())) for _ in range(10)]

# 1*1 ~ 5*5 색종이 각 5장
paper = [5, 5, 5, 5, 5]  # 아예 이렇게 한 리스트로 관리?

# visited = [[0] * 10 for _ in range(10)]
# 1. 모든 칸 탐색 (1 찾을 때까지)
# 2. 1 찾으면 모든 크기 색종이 부착 시도 => 0 나오면 fail
# 3. 부착
# 4. 제거

# 최종 결과 저장
min_ans = float('inf')


def can_attach_paper(x, y, size):
    """
    주어진 위치 (x, y)에서 size 크기의 색종이를 붙일 수 있는지 확인
    """
    for i, j in product(range(size), repeat=2):
        if x + i >= 10 or y + j >= 10 or not board[x + i][y + j]:
            return False
    return True


def update_paper(x, y, size, is_attach):
    """
    주어진 위치 (x, y)에서 size 크기의 색종이를 붙이거나 제거
    """
    for i, j in product(range(size), repeat=2):
        board[x + i][y + j] = 0 if is_attach else 1


def dfs(x, y, attach_cnt):
    """
    DFS를 통해 최소 색종이 개수를 찾는 함수
    """
    global min_ans

    # 1을 찾을 때까지 x와 y를 증가시킴
    while x < 10 and board[x][y] == 0:
        y += 1
        if y >= 10:
            x += 1
            y = 0

    # 모든 보드를 탐색한 경우
    if x >= 10:
        min_ans = min(min_ans, attach_cnt)
        return

    # 가지 치기
    if attach_cnt >= min_ans:
        return

    # 5부터 1까지의 색종이 크기를 시도
    for s in range(5, 0, -1):
        # 범위를 벗어나거나 해당 크기의 색종이가 모두 사용된 경우
        if x + s > 10 or y + s > 10 or paper[s - 1] == 0:
            continue

        # 색종이를 붙일 수 있는지 확인
        if can_attach_paper(x, y, s):
            # 색종이 부착
            update_paper(x, y, s, True)
            paper[s - 1] -= 1
            dfs(x, y, attach_cnt + 1)
            # 색종이 제거
            update_paper(x, y, s, False)
            paper[s - 1] += 1


# 초기 상태 설정 및 DFS 시작
dfs(0, 0, 0)

# 결과 출력
if min_ans == float('inf'):
    min_ans = -1
print(min_ans)
