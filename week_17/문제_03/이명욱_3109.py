def dfs(sr, sc):
    # 가장 오른쪽 끝에 도착하면 true 반환
    if sc == c-1:
        return True
    # 대각선 오른쪽 위, 오른쪽, 대각선 오른쪽 아래 순으로 탐색
    for dr in [-1, 0, 1]:
        nr = sr + dr
        nc = sc + 1
        # 범위 내이고
        if 0 <= nr < r and 0 <= nc < c:
            # 건물이 있는 곳이 아니고 방문 하지 않은 곳이라면
            if lst[nr][nc] != "x" and visited[nr][nc] == 0:
                # 다음 지점으로 이동
                visited[nr][nc] = 1
                if dfs(nr, nc):
                    return True
    # 이동 불가시 false 반환
    return False


r, c = map(int, input().split())

visited = [[0] * c for _ in range(r)]
lst = [list(input()) for _ in range(r)]

answer = 0
for i in range(r):
    if dfs(i,0):
        answer += 1
print(answer)