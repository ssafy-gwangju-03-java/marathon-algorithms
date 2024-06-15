def mario():
    dp = [[-10001] * (n + 1) for _ in range(t)]

    for i in range(s):
        dp[0][i] = arr[i]

    for i in range(t - 1):
        for j in range(n):
            if dp[i][j] != -10001:
                for k in range(1, s + 1):
                    if j + k >= n: # 넘어가는 경우
                        dp[i + 1][n] = max(dp[i + 1][n], dp[i][j])
                    else:
                        dp[i + 1][j + k] = max(dp[i + 1][j + k], dp[i][j] + arr[j + k])

    return dp[-1][-1]


while True:
    lst = list(map(int, input().split())) # 리스트로 입력받아서 개수 체크
    if lst[0] == 0: # 첫 입력값이 0이면 break
        break
    n = lst[0]
    s = lst[1]
    t = lst[2]
    arr = []
    cnt = 0
    while True:
        line = list(map(int, input().split()))
        arr += line
        # print(arr)
        cnt += len(line) 
        if cnt == n: # n개 입력 들어왔을 때 break 후 mario
            break
    print(mario())
