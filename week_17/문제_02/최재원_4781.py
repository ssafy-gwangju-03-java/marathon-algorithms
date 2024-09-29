import sys

sys.stdin = open("../../input.txt")
input = sys.stdin.readline

while True:
    arr = []
    n, m = input().split()
    n, m = int(n), int(float(m) * 100 + 0.5)
    if n == 0:
        break

    for i in range(int(n)):
        c, p = map(float, input().split())
        arr.append((int(c), int(float(p) * 100 + 0.5)))

    dp = [0] * (m + 1)
    for i in range(n):
        c, p = arr[i]

        for j in range(p, m + 1):
            dp[j] = max(dp[j], dp[j - p] + c)

    print(dp[m])
