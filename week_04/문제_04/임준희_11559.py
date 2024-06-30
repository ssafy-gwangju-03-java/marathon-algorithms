def chain_reaction(field):
    def dfs(x, y, color, visited):
        # 연결된 같은 색 뿌요 찾기
        if x < 0 or x >= 12 or y < 0 or y >= 6 or field[x][y] != color or visited[x][y]:
            return 0
        visited[x][y] = True
        count = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            count += dfs(x + dx, y + dy, color, visited)
        return count

    def remove():
        # 4개 이상 연결된 뿌요 제거
        visited = [[False] * 6 for _ in range(12)]
        removed = False
        for i in range(12):
            for j in range(6):
                if field[i][j] != '.' and not visited[i][j]:
                    if dfs(i, j, field[i][j], visited) >= 4:
                        remove_group(i, j, field[i][j])
                        removed = True
        return removed

    def remove_group(x, y, color):
        # 연결된 뿌요 그룹 제거
        if x < 0 or x >= 12 or y < 0 or y >= 6 or field[x][y] != color:
            return
        field[x][y] = '.'
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            remove_group(x + dx, y + dy, color)

    def gravity():
        # 중력 적용
        for j in range(6):
            stack = []
            for i in range(11, -1, -1):
                if field[i][j] != '.':
                    stack.append(field[i][j])
                    field[i][j] = '.'
            for i in range(11, 11 - len(stack), -1):
                field[i][j] = stack[11 - i]

    chains = 0
    while remove():
        chains += 1
        gravity()
    return chains

field = [list(input().strip()) for _ in range(12)]

print(chain_reaction(field))