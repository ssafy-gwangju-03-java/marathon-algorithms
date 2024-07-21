import sys
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

def solution():
    if N == 1:
        return arr[0]

    answer = 0
    i = 0

    while i < len(arr):
        if i == N - 1:
            answer += arr[i]
            return answer

        a = arr[i]
        b = arr[i + 1]

        if b <= 0:
            answer += a * b
            i += 2
        elif a > 1 and (N - i) % 2 == 0:
            answer += a * b
            i += 2
        else:
            answer += a
            i += 1

    return answer


print(solution())
