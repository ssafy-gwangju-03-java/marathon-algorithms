N = int(input())
lst = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열의 길이를 저장할 리스트
dp = [1] * N

for i in range(N):
    for j in range(i):
        # 만약 현재 수가 이전 수보다 크다면
        if lst[i] > lst[j]:
            # 최대값 비교
            dp[i] = max(dp[i], dp[j] + 1)

# 부분 수열 입력할 리스트
result = []
max_index = max(dp)
print(max_index)

for i in range(N - 1, -1, -1):
    # max_index의 해당하는 값 삽입하기
    if dp[i] == max_index:
        result.append(lst[i])
        # 삽입 후 index 1 감소
        max_index -= 1

# 큰 수부터 들어가 있어서 뒤집어서 출력
result.reverse()

print(*result)