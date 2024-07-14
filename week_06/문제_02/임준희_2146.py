from collections import deque

def find_island_edges(x, y, island_id):
    q = deque([(x, y)])
    visited[x][y] = island_id
    edges = []
    
    while q:
        x, y = q.popleft()
        is_edge = False
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if map_data[nx][ny] == 0:  # 인접한 칸이 바다인 경우
                    is_edge = True
                elif not visited[nx][ny]:  # 방문하지 않은 육지인 경우
                    visited[nx][ny] = island_id
                    q.append((nx, ny))
        
        if is_edge:
            edges.append((x, y))
    
    return edges

def shortest_bridge_length(start_island):
    q = deque(start_island)
    distance = [[-1] * size for _ in range(size)]
    
    for x, y in start_island:
        distance[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if visited[nx][ny] != 0 and visited[nx][ny] != visited[start_island[0][0]][start_island[0][1]]:
                    # 다른 섬에 도달한 경우
                    return distance[x][y]
                if map_data[nx][ny] == 0 and distance[nx][ny] == -1:  # 방문하지 않은 바다인 경우
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    
    return float('inf')  # 다리를 만들 수 없는 경우

size = int(input())
map_data = [list(map(int, input().split())) for _ in range(size)]
visited = [[0] * size for _ in range(size)]
islands = []
island_id = 1

for i in range(size):
    for j in range(size):
        if map_data[i][j] == 1 and not visited[i][j]:
            island_edges = find_island_edges(i, j, island_id)
            islands.append(island_edges)
            island_id += 1

min_bridge_length = float('inf')
for i in range(len(islands)):
    bridge_length = shortest_bridge_length(islands[i])
    min_bridge_length = min(min_bridge_length, bridge_length)

print(min_bridge_length)