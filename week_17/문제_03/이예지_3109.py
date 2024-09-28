# 3109 사탕가게
import sys
input = sys.stdin.readline

# 파이프 최대 개수
def dfs(i, j):
    if j == c - 1:
        return True

    for di, dj in move:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and maps[ni][nj] == '.':
            maps[ni][nj] = 'x'  # 방문 표시로 x 바꾸기
            if dfs(ni, nj):
                return True
    return False

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]     # x: 건물 있음
move = [(-1, 1), (0, 1), (1, 1)]    # 우상, 우, 우하 (이동 순서 중요 - 위쪽 먼저 가야 최대 개수 가능)
ans = 0

# 첫 열에서 마지막 열까지 dfs
for x in range(r):
    if dfs(x, 0):
        ans += 1

print(ans)