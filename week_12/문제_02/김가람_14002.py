import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 각 숫자마다의 LIS의 길이를 Memoization
memo = [0] * N

# 완성된 LIS를 저장해 줄 배열
LIS = [[] for _ in range(N)]

for i in range(N):
    memo[i] = 1
    LIS[i].append(nums[i])

    for j in range(i, -1, -1):
        if nums[j] < nums[i] and memo[i] < memo[j] + 1:
            # LIS 길이 비교
            memo[i] = memo[j] + 1
            # LIS 갱신
            NEW_LIS = []
            for num in LIS[j]:
                NEW_LIS.append(num)
            NEW_LIS.append(nums[i])
            LIS[i] = NEW_LIS

max_length = max(memo)

print(max_length)
for arr in LIS:
    if len(arr) == max_length:
        print(*arr)
        break
