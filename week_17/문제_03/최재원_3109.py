import sys

sys.stdin = open("../../input.txt")
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]


def dfs(r, c):
    global answer, finish

    if c == C - 1:  # 오른쪽 끝에 도달하면 정답 + 1
        answer += 1
        finish = True  # 파이프라인이 만들어졌다는 플래그
        return

    for i in (-1, 0, 1):  # 그리디로 위로, 그냥, 아래로 순서대로 탐색
        nr = r + i
        nc = c + 1

        # 파이프라인이 만들어지지 않았으면
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == '.' and not finish and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)


visited = [[False] * C for _ in range(R)]

answer = 0
for i in range(R): # (0,0)부터 (r-1,0)까지 dfs
    finish = False
    visited[i][0] = True
    dfs(i, 0)

print(answer)
