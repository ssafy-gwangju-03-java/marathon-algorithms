import sys
from copy import deepcopy

global m

# 맵 크기, 이동 횟수
X, m = map(int, sys.stdin.readline().rstrip().split())

# 맵 정보
MAP = []

# 이동 경로
M = []

# 맵 정보 입력
for i in range(X): MAP.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 방문체크 리스트
visit = deepcopy(MAP)

# 이동 경로 입력
for i in range(m): M.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 델타배열
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 시작 위치 설정
s0, s1 = M[0]

# DFS
def dfs(pos, idx):
    y, x = pos
    a = 0
    if not visit[y][x]:
        # 목표 위치 도달 확인
        if [y+1, x+1] == M[idx]:
            if idx == m-1:
                return 1
            else:
                a += dfs(pos, idx+1)
                return a
        # 방문 처리
        visit[y][x] = 1
        # 상하좌우 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < X and 0 <= ny < X:
                a += dfs([ny, nx], idx)
        # 방문 취소 (백트래킹)
        visit[y][x] = 0
    return a

print(dfs([s0-1, s1-1], 0))