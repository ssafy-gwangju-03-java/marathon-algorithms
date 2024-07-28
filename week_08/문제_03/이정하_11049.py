# 행렬 개수 N
N = int(input())
# N개의 행렬의 크기 r과 c
size = [list(map(int, input().split())) for _ in range(N)]

# 5*3 행렬 곱하기 3*2 행렬 => 5 * 3 * 2 번 & 5*2 행렬

# dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱하는데 필요한 최소 연산 횟수
dp = [[0] * N for _ in range(N)]

for l in range(1, N):  # l은 곱할 행렬의 개수 - 1
    for i in range(N - l):  # i는 시작 행렬의 인덱스
        j = i + l  # j는 마지막 행렬의 인덱스
        dp[i][j] = min(dp[i][k] + dp[k + 1][j] + size[i][0] * size[k][1] * size[j][1] for k in range(i, j))

print(dp[0][N - 1])  # 0번째부터 N-1번째까지 곱하는데 필요한 최소 연산 횟수 출력
