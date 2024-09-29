import sys

input = sys.stdin.readline
ans = 0  # 파이프라인 개수


def dfs(x, y):
    if y == C - 1:  # 마지막 열 도착하면 == 파이프라인 완성
        return True  # 설치 성공
    for dx in [-1, 0, 1]:  # 우상, 우, 우하 순회
        nx = x + dx
        ny = y + 1
        if 0 <= nx < R and 0 <= ny < C:  # 범위 내에 있으면
            if board[nx][ny] != "x" and visited[nx][ny] == -1:
                # 건물이 없고 방문하지 않은 칸인 경우
                visited[nx][ny] = 1  # 방문 처리
                if dfs(nx, ny):  # 다음 칸에서 DFS 실행
                    return True  # 파이프라인 설치 성공시 true
    return False  # 모든 방향을 시도했지만 실패한 경우 False 


# 행, 열 개수
R, C = map(int, input().split())
visited = [[-1 for _ in range(C)] for _ in range(R)]
board = [list(input().strip()) for _ in range(R)]  # 빵집 근처 모습
for i in range(R):  # 모든 행에 대해
    if dfs(i, 0): ans += 1  # 첫 번째 열에서 시작해서 DFS 실행, 성공하면 ans ++
print(ans)
