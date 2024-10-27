# 2473 세 용액


def sol():
    check = 3000000001
    p, q, r = 0, 0, 0
    for i in range(n - 2):
        start = i + 1
        end = n - 1
        while start < end:
            sum = lst[i] + lst[start] + lst[end]
            abssum = abs(sum)
            if sum == 0:
                p, q, r = lst[i], lst[start], lst[end]
                break
            if abssum < check:
                check = abssum
                p, q, r =lst[i], lst[start], lst[end]
            if sum > 0:
                end -= 1
            else:
                start += 1

    return p, q, r


n = int(input())
lst = list(map(int, input().split()))
lst.sort()
p, q, r = sol()
print(p, q, r)
