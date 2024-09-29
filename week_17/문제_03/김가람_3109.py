import sys

R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip("\n")) for _ in range(R)]

def dfs(r, c):
    global ans
    global did_reach

    if c == C - 1:
        if not did_reach:
            did_reach = True
            ans += 1
        return

    # 그리디하게 위쪽 방향부터 탐색, 최대한 많은 공간을 남겨두기 위함
    for next in (-1, 0, 1):
        nr, nc = r + next, c + 1
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 'x' and not did_reach:
            # 방문 흔적을 남기며 탐색, C - 1까지 도달 못하는 경로까지 미리 차단
            grid[nr][nc] = 'x'
            dfs(nr, nc)

ans = 0

for i in range(R):
    did_reach = False
    grid[i][0] = 'x'
    dfs(i, 0)

print(ans)