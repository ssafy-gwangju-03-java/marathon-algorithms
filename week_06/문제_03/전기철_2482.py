n = int(input())
k = int(input())
dp = [[0] * (k + 1) for _ in range(n + 1)]  # dp[n][k] -> n개 색 k개 선택 경우의 수

for i in range(n + 1):
    dp[i][0] = 1  # 안고르는건 1가지
    dp[i][1] = i  # 1개 고르는건 i가지

for i in range(4, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1])  
        # dp[i-1][j]에서 선택 안하는 종이 하나 추가하는 경우 + dp[i-2][j-1] 에서 추가하는 경우 ex) A점과 A+1점 사이 두칸을 붙인 후 하나에 색칠하는 경우
        # 추가설명 -> A칸에 색칠되어있는 경우 -> A+1은 색칠x -> A A+1 사이에 색칠X색칠O 종이 끼워넣기 / 반대도 똑같이 진행
print(dp[n][k] % 1000000003)
