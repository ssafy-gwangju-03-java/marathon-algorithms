import sys

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 차이를 저장
diff = []
for i in range(N - 1):
    diff.append(arr[i + 1] - arr[i])
diff.sort()

# 차이가 작은 순서대로 더하기
answer = 0
for i in range(N - K):
    answer += diff[i]
print(answer)


