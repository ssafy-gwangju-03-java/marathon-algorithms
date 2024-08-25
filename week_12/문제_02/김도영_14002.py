# 가장 긴 증가하는 부분수열 4

A_size = int(input())
A = list(map(int, input().split()))

dp = [1] * A_size
prev = [-1] * A_size

# 가장 긴 증가하는 부분 수열 길이 찾기
for i in range(1, A_size):
    for j in range(i):
        if A[j] < A[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

max_length = max(dp)

# 가장 긴 증가하는 부분 수열 찾기
lis = []
index = dp.index(max_length)
while index != -1:
    lis.append(A[index])
    index = prev[index]

lis.reverse()

print(max_length)
print(' '.join(map(str, lis)))