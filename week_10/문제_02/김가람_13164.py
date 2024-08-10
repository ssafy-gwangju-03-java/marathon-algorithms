import sys

N, K = map(int, sys.stdin.readline().split())
children = list(map(int, sys.stdin.readline().split()))

diff = []

# 각 아이들 사이에 벽이 있다고 가정하면, 벽을 없애면 얻는 값은 i + 1번째 아이의 키 - i번째 아이의 키
for i in range(N - 1):
    diff.append(children[i + 1] - children[i])

diff.sort()

# (N - 1) - (구하는 값) = (K - 1)
# == N - 1개의 벽에서 K - 1개의 벽만 남겨야 하므로, 벽은 N - K개 없애야 한다
print(sum(diff[:N - K]))