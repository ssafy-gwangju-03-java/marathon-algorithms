b = list(map(int, input().split()))

dp = [[False] * 501 for _ in range(501)]

for i in range(501):
    for j in range(501):

        for k in range(3):
            if i >= b[k] and not dp[i - b[k]][j]:
                dp[i][j] = True
                break

        for k in range(3):
            if j >= b[k] and not dp[i][j - b[k]]:
                dp[i][j] = True
                break

for _ in range(5):
    k1, k2 = map(int, input().split())

    if dp[k1][k2]:
        print('A')
    else:
        print('B')
