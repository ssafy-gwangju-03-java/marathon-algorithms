# 15989 1,2,3 더하기 4
import sys
input = sys.stdin.readline

def solve():
    dp = [1] * 10001    # 초기화

    # 2, 3 사용하는 경우
    for i in range(2, 10001):
        dp[i] += dp[i-2]
    for i in range(3, 10001):
        dp[i] += dp[i-3]

    return dp

# 미리 계산
result = solve()

t = int(input())
for _ in range(t):
    n = int(input())
    print(result[n])