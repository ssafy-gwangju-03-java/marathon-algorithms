# https://www.acmicpc.net/problem/14466

## Referenced
# https://github.com/ssafy-gwangju-03-java/marathon-algorithms/blob/main/week_04/%EB%AC%B8%EC%A0%9C_02/%EC%A0%84%EA%B8%B0%EC%B2%A0_14466.py

import sys
from collections import deque

input = sys.stdin.readline
N, K, R = map(int, input().split())

"""
경로 저장용 4차원 배열 생성
- Python 구현 특성 상 정수는 28바이트, 참조 포인터 8바이트이므로
  이론상 메모리 사용량은 약 2.8GB, 실 사용량은 ~900MB이기 때문에 사용하면 안되는 방법
- Python은 배열 내부 원소로 배열을 저장할 수 있기에, 2차원 배열 생성 후 각 좌표마다
  이어진 경로를 양방향 저장하는 방식이 효율적
"""
adjm = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(r, c):
    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N

    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        sr, sc = q.popleft()
        for i in range(4):
            nr, nc = sr + d[i][0], sc + d[i][1]
            if is_valid(nr, nc) and not adjm[sr][sc][nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1


for r in range(R):
    sr, sc, tr, tc = map(int, input().split())
    adjm[sr - 1][sc - 1][tr - 1][tc - 1] = 1
    adjm[tr - 1][tc - 1][sr - 1][sc - 1] = 1

cows = []
for k in range(K):
    r, c = map(int, input().split())
    cows.append((r - 1, c - 1))

count = 0
for i in range(K - 1):
    cow_from = cows[i]
    # BFS 계산 후 도달하지 못한 좌표를 확인하기 위해 방문 배열을 함수 외부에 배치
    visited = [[0] * N for _ in range(N)]
    bfs(cow_from[0], cow_from[1])

    # 중복 계산 방지용 시작 값 설정
    for j in range(i + 1, K):
        cow_to = cows[j]
        if not visited[cow_to[0]][cow_to[1]]:
            count += 1

print(count)
