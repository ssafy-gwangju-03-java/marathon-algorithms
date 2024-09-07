import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

gaps = []
for i in range(N - 1):
    gap = arr[i + 1] - arr[i]
    gaps.append(gap)

gaps.sort()

answer = 0
for i in range(N - K):
    answer += gaps[i]
print(answer)
