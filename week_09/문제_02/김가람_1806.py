import sys

N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

curr_sum = seq[0]
min_length = N + 1

# 투포인터 : left, right
l, r = 0, 0

while True:
    if curr_sum >= S:
        min_length = min(min_length, r - l + 1)
        if min_length == 1:
            break
        curr_sum -= seq[l]
        l += 1
    else:
        r += 1
        if r == N:
            break
        curr_sum += seq[r]

print(min_length if min_length != N + 1 else 0)
