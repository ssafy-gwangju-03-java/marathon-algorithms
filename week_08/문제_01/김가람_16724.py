import sys
sys.setrecursionlimit(10 ** 8)

N, M = map(int, sys.stdin.readline().split())
dir_char = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dir_coords = {
    "D": (1, 0),
    "U": (-1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

# start_point : dfs의 시작점 == (i, j)
# curr_point : 현재 dfs가 탐색하는 지점 == (i, j)
# path : 현재 dfs가 지나온 좌표들을 담은 리스트 == [(i, j), (i, j), ...]
# char : 현재 방향을 나타내는 문자 == "D" || "U" || "L" || "R"
def dfs(start_point, curr_point, path, char):
    global count

    # 만약 현재 도착한 지점이 이미 cycle에 포함된 곳이라면
    # 지금까지의 경로를 cycle에 포함시켜준 후 return
    if cycle[curr_point[0]][curr_point[1]]:
        for coords in path:
            cycle[coords[0]][coords[1]] = True
        return

    # 만약 이미 지나온 길로 또 돌아왔다면
    # 지금까지의 경로를 cycle에 포함시켜준 후 count를 증가시켜준 후 return
    if curr_point in path:
        for coords in path:
            cycle[coords[0]][coords[1]] = True
        count += 1
        return

    # 경로에 현재 좌표를 append
    path.append(curr_point)

    nr, nc = curr_point[0] + dir_coords[char][0], curr_point[1] + dir_coords[char][1]
    dfs(start_point, (nr, nc), path, dir_char[nr][nc])


cycle = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if not cycle[i][j]:
            dfs((i, j), (i, j), [], dir_char[i][j])

print(count)
