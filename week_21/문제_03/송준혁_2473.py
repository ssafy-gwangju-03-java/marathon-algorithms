# https://www.acmicpc.net/problem/2473

## Referenced
# https://beginthread.tistory.com/158

import sys

input = sys.stdin.readline


def mixer():
    min_value = 4000000001

    # 0 ~ (N - 3) 구간에서 기준점 i 설정
    for i in range(N - 3, -1, -1):

        # i 구간 이후 기준으로 양 끝단에 투 포인터를 지정
        l, r = i + 1, N - 1

        while l < r:
            sum_val = arr[i] + arr[l] + arr[r]
            tmp = abs(sum_val)

            # 세 개의 합이 현재의 최소값보다 작으면 갱신
            if min_value > tmp:
                solution[0], solution[1], solution[2] = i, l, r
                min_value = tmp

            # 합이 0이면 최소값이므로 탐색 종료
            if sum_val == 0:
                return

            # 합이 0보다 크다면 오른쪽 포인터 감소
            elif sum_val > 0:
                r -= 1

            # 합이 0보다 작으면 왼쪽 포인터를 증가
            else:
                l += 1


N = int(input())
arr = list(map(int, input().split()))
solution = [0] * 3

arr.sort()
mixer()

for i in range(3):
    print(arr[solution[i]], end=" ")
