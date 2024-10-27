def find(n, nums):
    result = [1e9, 1e9, 1e9]
    for i in range(n):
        # 포인터 설정
        l, r = i+1, n-1

        # 포인터 만날때 까지 반복
        while l < r:
            # 세 수의 합이 0이 되는 것이 없을 경우를 대비해 0과 가장 가까운 세 수의 합을 찾아낸다.
            if abs(sum(result)) > abs(nums[i] + nums[l] + nums[r]):
                result = [nums[i], nums[l], nums[r]]

            if nums[i] + nums[l] + nums[r] == 0:
                return nums[i], nums[l], nums[r]
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return result[0], result[1], result[2]


n = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(*find(n, lst))