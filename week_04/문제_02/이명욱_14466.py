# 소가 길을 건너간 이유 6
# 참고 : https://ryu-e.tistory.com/36
# enumerate : 반복 가능한 객체를 인자로 받앙서 해당 객체의 요소들을 순회하면서,
# 각 요소의 인덱스와 값을 순서쌍으로 반환하는 함수
# enumerate(iterable, start) // start: 인덱스 시작값, default 0
# for index, alpa in enumerate(["A", "B", "C"]):
#   print(index, alpa)
# 출력:
# 0 A
# 1 B
# 2 C

import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 소가 길을 건너지 않고 방문할 수 있는 목초지 탐색
def bfs(r1, c1):
    dq = deque()
    dq.append((r1, c1))
    cow_visit[r1][c1] = True
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if cow_visit[nx][ny]:  # 방문 체크
                continue
            if (nx, ny) in road[x][y]:  # 다리인 경우 pass
                continue
            dq.append((nx, ny))
            cow_visit[nx][ny] = True

# n*n, k: 마리, r: 정해진 길
n, k, r = map(int, sys.stdin.readline().split())

# 길 위치 입력받기
road = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(r):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

# 소 위치 입력받기
cow_list = list()
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    cow_list.append((a - 1, b - 1))

count = 0
# 1. 소 방문 여부 탐색
for i, cow in enumerate(cow_list):
    cow_visit = [[False] * n for _ in range(n)]
    # 2. 현재 소가 길을 건너지 않고 가는 경로를 탐색
    bfs(cow[0], cow[1])
    for r2, c2 in cow_list[i + 1:]:
        # 3. 소 끼리 방문하지 못한 경우 결과 + 1
        if not cow_visit[r2][c2]:
            count += 1
print(count)