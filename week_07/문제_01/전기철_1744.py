n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

ans = 0
idx = 0

while idx < n:

    if lst[idx] < 1:  # 음수 두번 or 음수 0 -> 곱해서 더함 / 음수 단일 -> 그냥 더함
        if idx + 1 < n and lst[idx + 1] < 1:
            ans += lst[idx] * lst[idx + 1]
            idx += 2
        else:
            ans += lst[idx]
            idx += 1
    else:
        # 이제부터 양수만
        # 양수 개수가 홀수면 처음꺼 그냥더하고 쭉 곱해주기
        if (n - idx) % 2:
            ans += lst[idx]
            idx += 1
        while idx < n:
            # 두 수 곱한거보다 더한게 큰 경우는 lst[idx]가 1인 경우만 존재
            if lst[idx] == 1:
                ans += lst[idx] + lst[idx + 1]
                idx += 2
            else:
                ans += lst[idx] * lst[idx + 1]
                idx += 2
print(ans)
