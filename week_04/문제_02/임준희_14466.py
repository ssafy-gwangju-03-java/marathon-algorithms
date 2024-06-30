from collections import deque

def bfs(start, roads, N):
    queue = deque([start])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= N and 1 <= nc <= N:  # 격자 내부인지 확인
                if (r, c, nr, nc) not in roads and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    return visited

N, K, R = map(int, input().split())

# 길 정보 저장
roads = set()
for _ in range(R):
    r, c, r2, c2 = map(int, input().split())
    roads.add((r, c, r2, c2))
    roads.add((r2, c2, r, c))  # 양방향 길

# 소의 위치 저장
cows = []
for _ in range(K):
    r, c = map(int, input().split())
    cows.append((r, c))

# 각 소마다 BFS 실행
reachable = []
for cow in cows:
    reachable.append(bfs(cow, roads, N))

# 만날 수 없는 소 쌍 계산
cannot_meet = 0
for i in range(K):
    for j in range(i+1, K):
        if cows[j] not in reachable[i]:
            cannot_meet += 1

print(cannot_meet)
