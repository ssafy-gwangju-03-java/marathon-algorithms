import sys
sys.stdin = open("../../input.txt", 'r')

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

p1, p2 = 0, 0
sum = 0
min_length = N + 1

while True:
    if sum >= S:
        min_length = min(p2 - p1, min_length)
        sum -= arr[p1]
        p1 += 1
    elif p2 == N:
        break
    else:
        sum += arr[p2]
        p2 += 1

print(min_length if min_length != N + 1 else 0)

