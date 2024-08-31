import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

seq = []

for _ in range(m):
    r, c = map(int, input().split())
    seq.append((r - 1, c - 1))

visited = [[False] * n for _ in range(n)]
visited[seq[0][0]][seq[0][1]] = True

answer = 0


def dfs(r, c, curr_point):
    global answer
    if (r, c) == (seq[m - 1][0], seq[m - 1][1]) and curr_point == m:
        answer += 1
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0 and not visited[nr][nc]:
            # 다음 타겟이면
            if (nr, nc) == seq[curr_point]:
                visited[nr][nc] = True
                dfs(nr, nc, curr_point + 1)
                visited[nr][nc] = False
            # 다음 타겟이 아니면
            else:
                visited[nr][nc] = True
                dfs(nr, nc, curr_point)
                visited[nr][nc] = False


dfs(seq[0][0], seq[0][1], 1)

print(answer)
