from collections import deque

# 교차로 N개, 걸리는시간 T
N, T = map(int, input().split())
# 교차로 신호 정보
intersections = [list(map(int, input().split())) for _ in range(N * N)]

# 방향 상우하좌
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 각 신호등 상태 12가지
signals = {
    1: [0, 1, 2], 2: [0, 1, 3], 3: [0, 2, 3], 4: [1, 2, 3],
    5: [0, 1], 6: [0, 3], 7: [2, 3], 8: [2, 3],
    9: [2, 3], 10: [0, 1], 11: [0, 3], 12: [2, 3],
}

# 0초, (0,0), 위쪽(상우하좌 0123)
queue = deque([(0, 0, 0, 0)])

visited = set()

# bfs
while queue:
    time, row, col, d = queue.popleft()

    # 시간이 T 초과하면 종료
    if time > T:
        break

    # 이번위치 범위 내 아니면 패스
    if not (0 <= row < N and 0 <= col < N):
        continue

    # 현재교차로 신호
    # 2차원 배열을 1차원으로 N*N 크기로 받았으니까 이렇게 접근해야 함...
    # 시간은 4개마다 신호 순환해야 해서 % 4
    cur_signal = intersections[row * N + col][time % 4]

    # 현재방향ㄴ, 현재신호 이동 가능 여부
    if d not in signals[cur_signal]:
        continue

    # 방문처리
    visited.add((row, col))

    # 다음 탐색
    for next_dir in signals[cur_signal]:
        nr = row + dirs[next_dir][0]
        nc = col + dirs[next_dir][1]
        queue.append((time + 1, nr, nc, next_dir))

print(len(visited))
