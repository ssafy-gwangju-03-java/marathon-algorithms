H, W = map(int, input().split())
lst = list(map(int, input().split()))
result = 0

for i in range(1, W-1):
    # 기준으로 왼쪽에 있는 블록 높이 최대값
    left = max(lst[:i])
    # 기준으로 오른쪽에 있는 블록 높이 최대값
    right = max(lst[i+1:])

    # 3 1 2 라면 1과 2의 차이 만큼 물이 고임
    min_v = min(left, right)
    if min_v - lst[i] > 0:
        result += (min_v - lst[i])

print(result)