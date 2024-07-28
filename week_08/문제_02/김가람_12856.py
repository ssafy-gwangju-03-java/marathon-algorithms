import sys

# 예전에 봤던 동영상 강의를 첨부합니다
# 이해 잘 안되는 분들은 15분만 투자해보세요!
# https://youtu.be/8LusJS5-AGo?si=Idbxk-2O7aiFQLRQ

N, K = map(int, sys.stdin.readline().split())
kg = [0] * (N + 1)
val = [0] * (N + 1)

# N번째 물건을 담는 경우와 담지 않는 경우의 val 값을 Memoization
memo = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    kg[i], val[i] = map(int, sys.stdin.readline().split())

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j - kg[i] >= 0:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - kg[i]] + val[i])
        else:
            memo[i][j] = memo[i - 1][j]

print(memo[N][K])
