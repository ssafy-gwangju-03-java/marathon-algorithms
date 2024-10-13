from itertools import combinations
from collections import deque

arr = [input().strip() for _ in range(5)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(selected):
    q = deque([selected[0]])
    visited = set([selected[0]])

    while q:
        nowy, nowx = q.popleft()

        for i in range(4):
            dy = nowy + di[i]
            dx = nowx + dj[i]

            # 선택된 7명에 포함되면서 방문하지 않은 경우
            if (dy, dx) in selected and (dy, dx) not in visited:
                visited.add((dy, dx))
                q.append((dy, dx))

    return len(visited) == 7

def find_groups():
    positions = [(i, j) for i in range(5) for j in range(5)]  #
    total_count = 0

    # 25명 중 7명을 선택하는 모든 조합 생성
    for comb in combinations(positions, 7):
        s_count = sum(1 for y, x in comb if arr[y][x] == 'S')

        if s_count >= 4 and dfs(comb):
            total_count += 1

    return total_count

print(find_groups())