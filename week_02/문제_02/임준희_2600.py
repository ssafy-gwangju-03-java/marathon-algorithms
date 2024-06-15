def game():
    for i in range(501):
        for j in range(501):
            for k in range(3):
                # 현재 i에서 b[k]를 뺀 값이 0 이상이고, 그 위치가 패배 위치면
                if i - b[k] >= 0 and dp[i - b[k]][j] == 0:
                    dp[i][j] = 1  # 현재 위치는 승리 위치로 설정
                # 현재 j에서 b[k]를 뺀 값이 0 이상이고, 그 위치가 패배 위치면
                if j - b[k] >= 0 and dp[i][j - b[k]] == 0:
                    dp[i][j] = 1  # 현재 위치는 승리 위치로 설정

b = list(map(int, input().split()))
dp = [[0] * 501 for _ in range(501)]

game()

for _ in range(5):
    k1, k2 = map(int, input().split())
    if dp[k1][k2]:
        print('A')
    else:
        print('B')