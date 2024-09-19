# https://www.acmicpc.net/problem/14002

## Referenced
# https://sjkoding.tistory.com/61
# https://sjkoding.tistory.com/62

import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

# dp[i]: i 위치의 값이 최장 길이 수열에 속할 때 그 값의 위치
dp = [1] * N
# q[i]: 최장 길이 수열에 속한 i 위치의 값 직전 값의 위치
q = [-1] * N

# 현재 위치 i와 i 이전의 위치 j 탐색
for i in range(1, N):
    for j in range(0, i):
        # i 위치의 값이 j 위치의 값보다 더 클 경우
        if arr[i] > arr[j]:
            # DP 배열에서 i의 위치보다 j의 위치 + 1이 더 클 경우
            # -> 현재 위치 i까지의 숫자로 만든 부분 수열이 더 길 경우
            if dp[i] < dp[j] + 1:
                # i의 순서와 i의 직전 순서 위치 갱신
                dp[i] = dp[j] + 1
                q[i] = j

max_length = max(dp)
max_index = dp.index(max_length)

arr_list = []
while max_index != -1:
    arr_list.append(arr[max_index])
    max_index = q[max_index]

print(max(dp))
print(*list(reversed(arr_list)))
