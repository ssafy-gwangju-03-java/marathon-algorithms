# 4781 사탕 가게
import sys
input = sys.stdin.readline

# 가진 돈으로 구매가능한 가장 높은 칼로리
def solve(n, m):
    m = int(m*100 + 0.5)    # rounding error 때문에
    dp = [0] * (m + 1)  # dp 리스트 생성 ; m으로 살 수 있는 최대 칼로리 계산 위해서

    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p*100 + 0.5)     # rounding error 때문에

        for i in range(p, m+1): # p~m까지 금액대 비교
            if dp[i] < dp[i - p] + c:
                dp[i] = dp[i - p] + c   # 큰 값을 dp[i]에

    return dp[-1]   # 최댓값은 dp 배열 맨 끝에 있으니까

while True:
    n, m = (input().split())    # n: 사탕 종류, m: 가진 돈
    n = int(n)
    m = float(m)
    ans = solve(n, m)
    if n == 0 and m == 0.00:
        break

    print(ans)