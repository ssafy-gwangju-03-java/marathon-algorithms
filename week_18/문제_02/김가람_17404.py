import sys, math

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = math.inf

# 첫번째 집에 각각 R, G, B를 선택하는 3가지 경우의 수 고려
for i in range(3):
    memo = [[math.inf] * 3 for _ in range(N)]
    memo[0][i] = cost[0][i]

    for j in range(1, N):
        memo[j][0] = cost[j][0] + min(memo[j-1][1], memo[j-1][2])
        memo[j][1] = cost[j][1] + min(memo[j-1][0], memo[j-1][2])
        memo[j][2] = cost[j][2] + min(memo[j-1][0], memo[j-1][1])

    # 첫번째 집과 다른 색일 경우에만 최솟값 갱신
    for j in range(3):
        if j != i:
            ans = min(ans, memo[N-1][j])

print(ans)