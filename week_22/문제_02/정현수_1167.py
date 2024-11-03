import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
V = int(data[0])
tree = [[] for _ in range(V + 1)]  

for i in range(1, V + 1):
    line = list(map(int, data[i].split()))
    node = line[0]
    idx = 1
    while line[idx] != -1:
        neighbor, distance = line[idx], line[idx + 1]
        tree[node].append((neighbor, distance))
        idx += 2

def bfs(start):
    distances = [-1] * (V + 1) 
    distances[start] = 0
    queue = deque([start])
    max_distance, max_node = 0, start

    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        for neighbor, distance in tree[node]:
            if distances[neighbor] == -1: 
                distances[neighbor] = current_distance + distance
                queue.append(neighbor)
                if distances[neighbor] > max_distance:
                    max_distance = distances[neighbor]
                    max_node = neighbor

    return max_node, max_distance

farthest_node, max_distance = bfs(1)  
max_distance, tree_diameter = bfs(farthest_node)  

print(tree_diameter)