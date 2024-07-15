# 수 묶기

N = int(input())

nums = [int(input()) for _ in range(N)]

nums.sort()

result = 0
idx = 0

while idx < N:
    # 0 또는 음수
    if nums[idx] < 1:
        # 다음 수 인덱스 검사 and 음수 * 음수
        if idx + 1 < N and nums[idx + 1] < 1:
            result += nums[idx] * nums[idx + 1]
            # 다음 수 까지 더했으니 idx + 2
            idx += 2
        else:
            result += nums[idx]
            idx += 1
    
    # 양수
    else:
        # 남은 양수의 갯수가 홀수
        if (N - idx) % 2 != 0:
            # 그냥 더하기
            result += nums[idx]
            idx += 1
        
        # 짝수 개 남음
        while idx < N:
            # 양수 * 양수 (곱하는 경우가 더 클 때)
            if nums[idx] * nums[idx + 1] > nums[idx] + nums[idx + 1]:
                result += nums[idx] * nums[idx + 1]
            
            else:
                result += (nums[idx] + nums[idx + 1])

            idx += 2
    
print(result)