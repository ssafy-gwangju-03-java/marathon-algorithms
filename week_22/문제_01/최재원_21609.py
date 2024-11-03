import sys
from collections import deque
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def find_largest_block_group(N, arr):
    visited = [[False] * N for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    largest_group = []
    max_rainbow_count = -1
    standard_block = (-1, -1)

    def bfs(r, c, color):
        queue = deque([(r, c)])
        group = [(r, c)]
        rainbow_blocks = []
        visited[r][c] = True
        rainbow_count = 0

        while queue:
            x, y = queue.popleft()

            for dr, dc in directions:
                nx, ny = x + dr, y + dc

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

                    if arr[nx][ny] == color or arr[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        group.append((nx, ny))

                        if arr[nx][ny] == 0:
                            rainbow_count += 1
                            rainbow_blocks.append((nx, ny))

        for x, y in rainbow_blocks:
            visited[x][y] = False

        return group, rainbow_count

    for i in range(N):
        for j in range(N):

            if arr[i][j] > 0 and not visited[i][j]:
                group, rainbow_count = bfs(i, j, arr[i][j])

                if len(group) >= 2:

                    standard_block_candidate = min((x, y) for x, y in group if arr[x][y] > 0)

                    if (len(group), rainbow_count, standard_block_candidate) > (len(largest_group), max_rainbow_count, standard_block):
                        largest_group = group
                        max_rainbow_count = rainbow_count
                        standard_block = standard_block_candidate

    return largest_group


def apply_gravity(N, arr):
    for col in range(N):
        empty_row = N - 1
        for row in range(N - 1, -1, -1):
            if arr[row][col] == -1:
                empty_row = row - 1
            elif arr[row][col] >= 0:
                if empty_row != row:
                    arr[empty_row][col] = arr[row][col]
                    arr[row][col] = -2

                empty_row -= 1


def rotate_counter_clockwise(N, arr):
    new_grid = [[-2] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[N - j - 1][i] = arr[i][j]
    return new_grid


def play_game(N, arr):
    total_score = 0
    while True:
        largest_group = find_largest_block_group(N, arr)

        if not largest_group:
            break

        for r, c in largest_group:
            arr[r][c] = -2
        total_score += len(largest_group) ** 2

        apply_gravity(N, arr)
        arr = rotate_counter_clockwise(N, arr)
        apply_gravity(N, arr)

    return total_score


result = play_game(N, arr)
print(result)
