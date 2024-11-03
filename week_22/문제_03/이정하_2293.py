# 1. 각 동전을 순차적으로 고려하면서
# 2. 해당 동전으로 만들 수 있는 모든 금액에 대해 경우의 수를 누적
# 3. dp 배열을 통해 각 금액을 만들 수 있는 경우의 수를 저장
# DP...?
n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

# dp 배열 초기화 (0부터 k원까지 표현하기 위해 k+1 크기로 생성)
dp = [0] * (k + 1)

# dp[0]을 1로 초기화
#   => 아무 동전도 사용하지 않는 경우
#   =>새로운 동전을 사용할 때 기준점으로 활용됨
dp[0] = 1

# 각 동전에 대해 반복
for coin in coins:
    # coin원부터 k원까지 반복
    # coin 미만의 금액은 현재 동전으로 만들 수 없으므로 건너뜀
    for i in range(coin, k + 1):
        # dp[i]: 현재 계산하고 있는 금액
        # dp[i - coin]: 현재 동전을 한 개 사용하기 전의 금액을 만드는 경우의 수

        # 예시: coin이 3이고 i가 5일 때
        # dp[5]에 dp[2]의 값을 더함 -> 2원을 만드는 방법에 3원을 추가하는 경우의 수
        possible_cases = dp[i - coin]

        # 현재까지의 경우의 수에 새로운 경우의 수를 누적
        dp[i] += possible_cases

# 최종적으로 k원을 만드는 모든 경우의 수
print(dp[k])