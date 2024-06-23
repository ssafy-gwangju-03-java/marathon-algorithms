# 내리막 길
def find(r, c):
    # 방문한 지점 계산 x
    if dp[r][c] != -1:
        return dp[r][c]
    # 목표 지점 1 반환
    if r == M - 1 and c == N - 1:
        return 1
    dp[r][c] = 0
    # 상하좌우 이동
    for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        # 범위 내, 높이가 낮은 지점으로 이동
        if 0 <= nr < M and 0 <= nc < N and lst[r][c] > lst[nr][nc]:
            # 이동 가능한 좌표들의 dp 값 더해주기
            dp[r][c] += find(nr, nc)
    return dp[r][c]

# 입력 받기
M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
# dp
dp = [[-1] * N for _ in range(M)]

print(find(0, 0))