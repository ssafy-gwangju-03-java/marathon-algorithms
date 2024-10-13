import sys
from collections import deque
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = 5
c = [0] * 7
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


# 7개를 뽑는 조합 만들기
def comb(idx, start):
    if idx == 7:
        # 규칙 확인
        validate(c)
        return

    for i in range(start, 25):
        c[idx] = i
        comb(idx + 1, i + 1)


def validate(selected_nums):
    global answer
    # 만들어진 조합을 인덱스로 변환
    students = comb_to_index(selected_nums)

    # S가 4개 이상이면
    if validate_SCount(students):
        temp = [[0] * N for _ in range(N)]

        for student in students:
            r, c = student
            temp[r][c] = 1

        count = 0
        visited = [[False] * N for _ in range(N)]

        # 한덩이인지 확인
        for i in range(N):
            for j in range(N):
                if temp[i][j] == 1 and not visited[i][j]:
                    count += 1
                    bfs(i, j, temp, visited)

        # 한덩이면 정답 += 1
        if count == 1:
            answer += 1

# 조합을 인덱스로 변환
def comb_to_index(selected_nums):
    students = []
    for num in selected_nums:
        r = num // 5
        c = num % 5
        students.append((r, c))
    return students


# S가 4개 이상인지 판별하는 함수
def validate_SCount(students):
    count = 0
    for r, c in students:
        if arr[r][c] == 'S':
            count += 1
    return count >= 4


def bfs(i, j, temp, visited):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            in_range = (0 <= nr < N and 0 <= nc < N)

            if in_range and temp[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True

answer = 0
arr = [list(input().strip()) for _ in range(N)]  # Ensure no extra spaces
comb(0, 0)
print(answer)
