import sys

# i가 1로만 이루어 진 경우의 수를 미리 넣어놓기
memo = [1] * 10001

# i가 ? + 2로 이루어진 경우의 수 갱신
for i in range(2, 10001):
    memo[i] += memo[i - 2]

# i가 ? + 3으로 이루어진 경우의 수 갱신
for i in range(3, 10001):
    memo[i] += memo[i - 3]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(memo[N])
