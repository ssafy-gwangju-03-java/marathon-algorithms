# https://www.acmicpc.net/problem/13164

## Referenced
# https://nanyoungkim.tistory.com/220

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
children = list(map(int, input().split()))

# 원생 간의 키 차이를 구함
diff = []
for i in range(N - 1, 0, -1):
    diff.append(children[i] - children[i - 1])

# N명을 K개 집단으로 나눌 경우 K - 1번 나누면 됨
# 키 차이를 오름차순 정렬 후 차이가 큰 순서대로 K - 1개를 제외
diff.sort()
for k in range(K - 1):
    diff.pop()

print(sum(diff))
