import sys

# https://www.youtube.com/watch?v=vgLJZMUfnsU
# https://kangminjun.tistory.com/entry/BOJ-11049%EB%B2%88-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C

N = int(sys.stdin.readline())
mat = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# i번부터 j번 까지의 행렬 곱의 최솟값을 Memoization
memo = [[0] * N for _ in range(N)]

# BASE: i번 행렬부터 i+1 행렬까지의 곱의 최솟값은 두 행렬의 곱셈의 값
for i in range(N-1):
    memo[i][i+1] = mat[i][0] * mat[i][1] * mat[i+1][1]

# 이후 두 행렬 사이의 gap이 2일때부터 DP 시작
# left == 곱셈 대상 중 왼쪽 행렬
# right == 곱셈 대상 중 오른쪽 행렬
for gap in range(2, N):
    for left in range(N - gap):
        right = left + gap

        memo[left][right] = 2e9

        """
        k == left 행렬과 right 사이의 중간값
        A, B, C, D 행렬이 있다고 가정하면
        A * BCD
        AB * CD
        ABC * D
        순서로 곱셈을 분할해준다
        """
        for k in range(left, right):
            memo[left][right] = min(memo[left][right], memo[left][k] + memo[k + 1][right] + mat[left][0] * mat[k][1] * mat[right][1])

print(memo[0][N-1])
