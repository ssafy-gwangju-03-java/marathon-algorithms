import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

seq = deque()
order = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == order:
        seq.appendleft(arr[i])
        order -= 1

print(max(dp))
print(*seq)
