# 14002 가장 긴 증가하는 부분수열 4
n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):  # 횟수 찾기
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
mx = max(dp)
print(mx)

# mx값을 기준으로 역추론 시작
ans = []
for i, size in enumerate(dp[::-1]):
    # print(i, size)
    if size == mx:
        ans.append(lst[n - i - 1])
        mx -= 1

print(*ans[::-1])
