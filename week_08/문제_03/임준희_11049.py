import sys

def res(d):
    n = len(d) - 1
    # dp[i][j]: i번째부터 j번째 행렬까지의 최소 곱셈 연산 수
    dp = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            # 초기값을 최대로 설정
            dp[i][j] = sys.maxsize
            
            for k in range(i, j):
                c = dp[i][k] + dp[k+1][j] + d[i] * d[k+1] * d[j+1]
                # 최소값 갱신
                if c < dp[i][j]:
                    dp[i][j] = c
    
    return dp[0][n-1]

n = int(input())
d = []
for _ in range(n):
    r, c = map(int, input().split())
    if not d:
        d.append(r)  # 첫 번째 행렬의 행 수 추가
    d.append(c)  # 각 행렬의 열 수 추가

# 결과 출력
print(res(d))