while True:
    n, m = map(float, input().split())
    # 부동 소수점 오류
    n, m = int(n), int(m * 100 + 0.5)

    # 루프 종료
    if n == 0 and m == 0:
        break

    dp = [0 for _ in range(m+1)]
    for _ in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)

        # 가격 p 부터 최대 금액 m까지 dp 배열 갱신
        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i-p] + c)

    print(dp[m])