import sys
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

properties = [0, 0, 0]
zero = float('inf')

for i in range(N - 2):
    left, right = i + 1, N - 1

    while left < right:
        total_sum = arr[i] + arr[left] + arr[right]

        if abs(total_sum) < zero:
            zero = abs(total_sum)
            properties[0], properties[1], properties[2] = arr[i], arr[left], arr[right]

        if total_sum > 0:
            right -= 1
        else:
            left += 1

print(*properties)
