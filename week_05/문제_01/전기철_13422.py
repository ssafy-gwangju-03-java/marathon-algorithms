t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    # n과 m이 같을 때
    if n == m:
        if sum(lst) < k:
            cnt += 1

    # 크기가 1인 경우
    elif m == 1:
        for i in range(n):
            if lst[i] < k:
                cnt += 1

    else:
        ans = sum(lst[:m]) # 합
        if ans < k:
            cnt += 1
        l = 0
        r = m
        while r < n + m - 1: # 이동하면서 왼쪽거 빼고 오른쪽거 더해주는 방식 반복
            ans -= lst[l % n]
            ans += lst[r % n]
            l += 1
            r += 1
            if ans < k:
                cnt += 1

    print(cnt)
