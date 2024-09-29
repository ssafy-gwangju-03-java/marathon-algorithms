# https://www.acmicpc.net/problem/4781

## Reference
# https://nahwasa.com/entry/백준-4781-자바-사탕-가게-BOJ-4781-JAVA

import sys

input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if n == 0:
        break

    # 반올림 오류 해결을 위해 100을 곱해 정수로 만들고 0.5를 더해줌
    # https://www.acmicpc.net/board/view/82054
    m = int(m * 100 + 0.5)
    # dp[i]: 가격 i로 살 수 있는 최대 칼로리 사탕
    dp = [0 for _ in range(m + 1)]

    for _ in range(int(n)):
        c, p = map(float, input().split())
        p = int(p * 100 + 0.5)

        for money in range(p, m + 1):
            # 현재 잔돈 money로 살 수 있는 최대 칼로리
            # 1. 기존에 저장된 칼로리
            # 2. p 가격의 사탕 구매 후의 칼로리 누적합
            # 둘 중 최대값
            dp[money] = max(dp[money], dp[money - p] + c)

    print(int(dp[m]))
