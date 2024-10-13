# [참고] https://youtu.be/DWdFSOehwFI?si=61gmsWRbq8olzQBI(문어박사 IT편의점)
from collections import deque

def bfs(sr, sc):
    q = deque()
    vv = [[0] * 5 for _ in range(5)]
    q.append((sr, sc))
    vv[sr][sc] = 1
    cnt = 1

    while q:
        sr, sc = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and vv[nr][nc] == 0 and v[nr][nc] == 1:
                q.append((nr, nc))
                vv[nr][nc] = 1
                cnt += 1
    return cnt == 7


def check():
    for r in range(5):
        for c in range(5):
            if v[r][c] == 1:
                return bfs(r, c)
def dfs(n, cnt, scnt):
    global ans
    # 가지치기: 이미 7명 넘었으면 7공주 불가
    if cnt > 7:
        return
    if n == 25:
        # 다솜파 4명 이상이면서 총 7명이면
        if cnt == 7 and scnt >= 4:
            # 인접 체크 후 모두 인접시 정답 +=1
            if check():
                ans += 1
            return

    # 포함하는 경우
    v[n//5][n%5] = 1
    dfs(n+1, cnt+1, scnt + int(arr[n//5][n%5] == 'S'))
    v[n//5][n%5] = 0

    # 포함하지 않는 경우
    dfs(n + 1, cnt, scnt)


arr = [input() for _ in range(5)]

ans = 0
v = [[0]*5 for _ in range(5)]
# 학생번호(0~24), 포함 학생수, 다솜파 학생수
dfs(0, 0, 0)
print(ans)