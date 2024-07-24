# 11049 행렬 곱셈 순서

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]  # dp[i][j] -> i~j 사이 연산 최소값 저장
INF = 1e9
for t in range(1, n):
    for i in range(n - t):
        now = i + t
        if t == 1:  # 차이가 1밖에 안남 -> 그냥 곱함
            dp[i][now] = lst[i][0] * lst[now][0] * lst[now][1]
            continue
        dp[i][now] = INF
        for k in range(i, now):
            dp[i][now] = min(dp[i][now],dp[i][k] + lst[i][0] * lst[k][1] * lst[now][1] + dp[k + 1][now])
            # 먼저 연산이 진행되는 위치 찾기
            # i~k 합 + k+1~now 합 -> i~now 합
            # i~k 행렬과 k+1~now 행렬 연산 -> lst[i][0]*lst[k][1]*lst[now][1]
            # 이렇게 접근을 하긴 했는데 맞는 접근인지는 모르겠다
            
print(dp[0][n - 1])
