# 수열의 크기 N
N = int(input())

# 수열
arr = list(map(int, input().split()))

# 각 위치에서 끝나는 LIS(Longest Increasing Subsequence)의 길이를 저장할 dp 배열
# dp[i]: i번째 원소를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
# => 초기값은 전부 1! 각 원소 자체로 길이 1의 부분 수열이 되니까
dp = [1] * N

# 각 위치에서 이전 원소의 인덱스를 저장할 배열
#  i번째 원소 이전에 오는 LIS의 원소의 인덱스를 저장 => 나중에 진짜 LIS 역추적
prev = [-1] * N


for i in range(1, N):
    for j in range(i): # i번보다 앞에 있는 모든 j에 대해
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            # 만약 이번꺼가 이전꺼보다 크고 && (이전까지의 LIS 길이+1)이 현재까지의 LIS 길이보다 크면
            dp[i] = dp[j] + 1 # i번째 갱신
            prev[i] = j # i의 이전 원소 인덱스를 j로 갱신

# dp배열에서 최대 LIS 길이랑 인덱스 찾기
max_length = max(dp)
max_index = dp.index(max_length)

# 실제 LIS를 역추적
lis = []
while max_index != -1:
    lis.append(arr[max_index]) # 현재 lis의 마지막 원소 
    max_index = prev[max_index] # lis의 이전 원소로

# LIS 역순으로 정렬해서 원래 순서대로
lis.reverse()

print(max_length)
print(*lis)