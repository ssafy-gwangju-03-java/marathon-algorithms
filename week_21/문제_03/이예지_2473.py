# 2473 세 용액
import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    solutions = list(map(int, input().split()))
    solutions.sort()  # 이분 탐색을 위한 정렬

    min_sum = float('inf')
    result = []

    # 첫 번째 용액을 고정하고 나머지 두 용액을 투 포인터로 찾기
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = solutions[i] + solutions[left] + solutions[right]

            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                result = [solutions[i], solutions[left], solutions[right]]

            # 합이 0보다 크면 right를 감소
            if current_sum > 0:
                right -= 1
            # 합이 0보다 작으면 left를 증가
            elif current_sum < 0:
                left += 1
            # 합이 0이면 바로 반환
            else:
                return result

    return result


ans = solve()
print(*ans)