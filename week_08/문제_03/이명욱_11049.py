# 참고 : https://ddiyeon.tistory.com/72

# 행렬의 개수 입력 받기
n = int(input())

# 각 행렬의 크기 입력 받기 (행, 열)
mat = [tuple(map(int, input().split())) for i in range(n)]

# dp 테이블 초기화, dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱셈하는 데 필요한 최소 곱셈 연산 수를 저장
dp = [[0] * n for i in range(n)]

# 행렬 곱셈 순서를 결정하는 부분
# cnt는 부분 문제의 크기 - 1 (즉, 행렬 범위의 길이 - 1)
for cnt in range(n - 1):
    # i는 시작 행렬의 인덱스
    for i in range(n - 1 - cnt):
        # j는 끝 행렬의 인덱스
        j = i + cnt + 1
        # dp[i][j]를 최대 값으로 초기화 (이후에 최소 값을 찾기 위해)
        dp[i][j] = 2 ** 31
        # k는 행렬 곱셈의 분할 지점
        for k in range(i, j):
            # dp[i][j]를 최소화하기 위해 dp[i][k]와 dp[k+1][j]의 값과 mat[i][0] * mat[k][1] * mat[j][1]을 더한 값 중 최소 값을 선택
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + mat[i][0] * mat[k][1] * mat[j][1])

# dp[0][n-1]에 저장된 값이 전체 행렬 곱셈 연산의 최소 곱셈 연산 수
print(dp[0][-1])
