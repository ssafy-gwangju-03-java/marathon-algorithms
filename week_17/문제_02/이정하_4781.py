# 사탕 가게에 있는 모든 사탕의 가격과 칼로리가 주어졌을 때,
# 어떻게 하면 칼로리의 합이 가장 크게 되는지

def process_input():
    # 빈 리스트를 생성하여 모든 테스트 케이스를 저장합니다.
    test_cases = []

    while True:  # 0 0.00 들어올때까지 반복
        # 사탕종류 N개, 돈의 양 M(항상 소수점 둘째자리)원
        n, m = map(float, input().split())

        # 종료조건
        if n == 0 and m == 0.00:
            break

        n = int(n)
        candies = []

        # 각 사탕의 칼로리 c와 가격 p
        # (1 ≤ c ≤ 5,000, 0.01 ≤ p ≤ 100.00) c는 항상 정수, p는 항상 소수점 둘째자리
        for _ in range(n):
            c, p = map(float, input().split())
            # 칼로리는 정수로
            candies.append((int(c), p))
        # print(candies)
        test_cases.append((m, candies))

    return test_cases


# dp로 최대 칼로리 계산
def max_calories(money, candies):
    # 정수 단위로 계산
    money = int(money * 100 + 0.5) # 반올림 <= 부동소수점 오류

    # 각 금액에 대해 얻을 수 있는 최대 칼로리 저장
    dp = [0] * (money + 1)

    # 모든 금액에 대해
    for i in range(1, money + 1):
        # 각각의 사탕에 대해
        for calories, price in candies:
            price = int(price * 100 + 0.5)# 가격 정수단위로, 반올림

            # # 역순으로 DP 갱신
            # for i in range(money, price - 1, -1):
            #     # 현재 사탕을 선택했을 때의 칼로리랑 선택하지 않았을 때의 칼로리 중 큰 값 선택
            #     dp[i] = max(dp[i], dp[i - price] + calories)
            # 현재 금액으로 사탕을 살 수 있는 경우
            if i >= price: # 각 금액에 대해 모든 사탕을 고려 -> 같은사탕 여러번 선택
                dp[i] = max(dp[i], dp[i - price] + calories)

    return dp[money]


test_cases = process_input()

for money, candies in test_cases:
    result = max_calories(money, candies)
    print(result)
