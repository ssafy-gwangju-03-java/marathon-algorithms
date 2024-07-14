import sys
input = sys.stdin.readline

N = int(input()) 
K = int(input())  

dp = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(N + 1):
    for j in range(min(i, K) + 1):
        # 아무 색도 선택하지 않는 경우의 수는 1
        if j == 0:
            dp[i][j] = 1
            continue
        
        # i개에서 색을 1개 선택하는 경우의 수는 i
        if j == 1:
            dp[i][j] = i
            continue
        
        # i번째 색을 선택하지 않는 경우
        dp[i][j] += dp[i - 1][j]
        
        # i번째 색을 선택하는 경우
        if i == N:  # 마지막 색을 선택할 때는 첫 번째와 두 번째 색을 선택할 수 없음
            dp[i][j] += dp[i - 3][j - 1]
        else:  # 그 외의 경우 바로 전 색만 선택할 수 없음
            dp[i][j] += dp[i - 2][j - 1]
        
        dp[i][j] %= 1000000003  

print(dp[N][K])