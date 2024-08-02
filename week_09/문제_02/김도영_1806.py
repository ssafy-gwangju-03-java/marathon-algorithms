# 부분합

N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_length = 1e9

# 슬라이딩 윈도우
start, end = 0, 0
sum = arr[start]
result = 1e9

while start < N:
    # 합이 S보다 작으면
    if sum < S:
        end += 1
        if end < N:
            sum += arr[end]

        else:
            break

    # 합이 S보다 크거나 같으면
    else:
        result = min(result, end - start + 1)
        sum -= arr[start]
        start += 1
    
print(0 if result == 1e9 else result)
