# https://www.acmicpc.net/problem/11559

import sys
from collections import deque

input = sys.stdin.readline
field = [list(str(input().rstrip())) for _ in range(12)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 뿌요 정리: 한 순회에서 모든 뿌요 뭉치를 없앤 이후, 열 우선 순회로
# 각 열에 남아있는 뿌요들을 스택에 넣고, 아래에서부터 역으로 채워넣기
def field_cleanup():
    for c in range(6):
        stack = []
        for r in range(12):
            if field[r][c] != ".":
                stack.append(field[r][c])
                field[r][c] = "."

        for r in range(11, 11 - len(stack), -1):
            field[r][c] = stack.pop()


def explode(r, c):
    """
    BFS 탐색으로 같은 색이 연속된 뿌요를 찾고,
    더 이상 연결된 같은 색이 없을 경우 4개 이상 연결된 모든 뿌요를 삭제
    """
    def is_valid(r, c):
        return 0 <= r < 12 and 0 <= c < 6

    q = deque()
    q.append((r, c))
    visited = [[0] * 6 for _ in range(12)]
    visited[r][c] = 1
    puyos = [(r, c)]

    while q:
        sr, sc = q.popleft()
        color = field[sr][sc]
        for i in range(4):
            nr, nc = sr + d[i][0], sc + d[i][1]
            if is_valid(nr, nc) and field[nr][nc] == color and not visited[nr][nc]:
                q.append((nr, nc))
                puyos.append((nr, nc))
                visited[nr][nc] = 1

    # 4개 이상 연속된 뿌요 뭉치가 있을 경우에만 삭제 후 1 반환
    if len(puyos) >= 4:
        for puyo in puyos:
            field[puyo[0]][puyo[1]] = "."
        return 1
    else:
        return 0


count = 0
# 순회 1번 -> 연쇄 1번
# 한 순회마다 4개 이상 연속된 뿌요 뭉치를 없애야하기 때문에,
# 연속된 모든 뿌요 뭉치를 없앤 이후 필드를 정리
# 더 이상 없앤 뿌요 뭉치가 없어 puyo_count가 0일 경우 루프 종료
while True:
    puyo_count = 0
    for r in range(12):
        for c in range(6):
            if field[r][c] != ".":
                puyo_count += explode(r, c)
    field_cleanup()
    if not puyo_count:
        break
    else:
        count += 1

print(count)
