from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 순환선 확인
def dfs(start, idx, cnt):
    global cycle
    # 방문한 역이 2곳 이상이고, 현재 역이 시작 역으로 돌아오면
    if start == idx and cnt >= 2:
        # 순환역 표시
        cycle = True
        return
    # 현재역 방문 표시
    visited[idx] = 1
    for i in lst[idx]:
        if not visited[i]:
            dfs(start, i, cnt + 1)
        elif i == start and cnt >= 2:
            dfs(start, i, cnt)

# 순환선 사이의 최소 거리
def bfs():
    global check
    q = deque()
    for i in range(N):
        # 순환역에 속하는 역은 모두 거리 0
        if circle_station[i]:
            check[i] = 0
            q.append(i)
    while q:
        now = q.popleft()
        for i in lst[now]:
            # 순환역에 포함되지 않는 역이라면
            if check[i] == -1:
                q.append(i)
                # 이동거리 더해서 저장
                check[i] = check[now] + 1


N = int(input())
lst = [[] for _ in range(N)]
# 순환역 표시 리스트
circle_station = [0] * N
# 정답 lst(순환선과의 거리)
check = [-1] * N

for _ in range(N):
    a, b = map(int, input().split())
    lst[a-1].append(b-1)
    lst[b-1].append(a-1)

# 순환선 확인
for i in range(N):
    # 방문 기록
    visited = [0] * N
    # 순환선 여부
    cycle = False
    # 순환선 탐색
    dfs(i, i, 0)
    # 순환역 확인
    if cycle:
        circle_station[i] = 1

# 순환선과의 거리 구하기
bfs()

# 모든 역의 순환선 사이의 거리 출력
print(*check)
