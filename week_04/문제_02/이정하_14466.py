import sys
from collections import deque

# 이동 방향 벡터 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# BFS 탐색 함수 정의
def bfs(r1, c1):
    dq = deque()  # 덱(deque) 초기화
    dq.append((r1, c1))  # 시작점 추가
    visited[r1][c1] = True  # 시작점 방문 처리
    while dq:  # 덱이 빌 때까지 반복
        r, c = dq.popleft()  # 현재 위치 꺼내기
        for d in range(4):  # 네 방향으로 이동 시도
            nr = dr[d] + r
            nc = dc[d] + c
            # 범위 체크
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc]:  # 이미 방문한 위치인지 체크
                continue
            if (nr, nc) in road[r][c]:  # 길이 있으면 패스
                continue
            dq.append((nr, nc))  # 다음 위치 추가하기
            visited[nr][nc] = True  # 방문 처리


# N*N 농장, 소 K마리, 길 R개
N, K, R = map(int, input().split())

# 길 정보 저장
road = [[[] for _ in range(N)] for _ in range(N)]  # 길 정보
visited = [[False] * N for _ in range(N)]  # 방문 여부
count = 0  # 결과값 초기화

# 길 정보 입력받기
for _ in range(R):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))  # 양방향 길 저장
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

# 소의 위치 입력받기
cow_list = list()
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    cow_list.append((a - 1, b - 1))  # 소의 위치 리스트에 추가

# 각 소에 대해서!!
for i, cow in enumerate(cow_list):
    visited = [[False] * N for _ in range(N)]  # 방문 여부 초기화
    bfs(cow[0], cow[1])  # BFS 수행
    for r2, c2 in cow_list[i + 1:]:  # 다른 소들과 비교
        if not visited[r2][c2]:  # 방문하지 못한 경우 카운트 증가
            count += 1

print(count)