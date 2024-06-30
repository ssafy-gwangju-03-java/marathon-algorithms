import sys
from collections import deque
sys.stdin = open("../input.txt")

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def fall(arr, N, M):
    # 열을 순서대로 검사
    for i in range(M):
        stack = []

        # 스택에 문자 추가하고 배열에서 제거
        for j in range(N):
            if arr[j][i] != '.':
                stack.append(arr[j][i])
                arr[j][i] = '.'

        # 스택에서 문자 다시 추가
        size = len(stack)
        for j in range(N - 1, N - size - 1, -1):
            arr[j][i] = stack.pop()


def bfs(i, j):
    color = arr[i][j]
    visited[i][j] = True

    recorder = [(i, j)]
    queue = deque([(i, j)])

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == color:
                queue.append((nr, nc))
                visited[nr][nc] = True
                recorder.append((nr, nc))

    # 4개 이상의 같은 색의 블록이 연결된 경우 붐 발생
    if len(recorder) >= 4:
        for r, c in recorder:
            arr[r][c] = '.'
        return True
    return False


N = 12
M = 6

arr = []
for _ in range(N):
    arr.append(list(sys.stdin.readline()))

answer = 0


while True:
    visited = [[False] * M for _ in range(N)]
    boom = False

    # 모든 셀을 탐색
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '.' and not visited[i][j]:
                if bfs(i, j):
                    boom = True

    if boom:
        answer += 1
    else:
        break

    fall(arr, N, M)

print(answer)
