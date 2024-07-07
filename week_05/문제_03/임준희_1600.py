from collections import deque

K = int(input())  # 말처럼 움직일 수 있는 횟수
W, H = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range(H)]

# 방문 여부를 저장할 3차원 배열 (x, y, k)
# k는 말처럼 움직인 횟수
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

# 말처럼 움직임
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 원숭이 움직임
monkey_dx = [0, 0, 1, -1]
monkey_dy = [1, -1, 0, 0]

def bfs():
    q = deque([(0, 0, 0, 0)])  # (x, y, 이동 횟수, 말처럼 이동한 횟수)
    visited[0][0][0] = True

    while q:
        x, y, moves, horse_moves = q.popleft()

        # 목적지에 도착한 경우
        if x == H - 1 and y == W - 1:
            return moves  # 최소 이동 횟수 리턴

        # 인접한 칸으로 이동
        for i in range(4):
            nx, ny = x + monkey_dx[i], y + monkey_dy[i]
            if 0 <= nx < H and 0 <= ny < W and not grid[nx][ny]:
                if not visited[nx][ny][horse_moves]:
                    visited[nx][ny][horse_moves] = True
                    q.append((nx, ny, moves + 1, horse_moves))

        # 말처럼 이동 (K번 미만으로 사용한 경우에만)
        if horse_moves < K:
            for i in range(8):
                nx, ny = x + horse_dx[i], y + horse_dy[i]
                if 0 <= nx < H and 0 <= ny < W and not grid[nx][ny]:
                    if not visited[nx][ny][horse_moves + 1]:
                        visited[nx][ny][horse_moves + 1] = True
                        q.append((nx, ny, moves + 1, horse_moves + 1))

    return -1  # 목적지에 도착할 수 없을때

result = bfs()
print(result)