# 구간합, 누적합

M, N = map(int, input().split())

K = int(input())

lst = [list(input()) for _ in range(M)]
# print(lst)
j_sum = [[0] * (N + 1) for _ in range(M + 1)]
o_sum = [[0] * (N + 1) for _ in range(M + 1)]
i_sum = [[0] * (N + 1) for _ in range(M + 1)]

# 전체 lst 순회하며 누적합 구해놓기
for i in range(1, M+1):
    for j in range(1, N+1):
        place = lst[i-1][j-1]
        # o, j, i 개수 세기
        if place == 'O':
            o_sum[i][j] += 1
        if place == 'J':
            j_sum[i][j] += 1
        if place == 'I':
            i_sum[i][j] += 1
        j_sum[i][j] = j_sum[i][j-1] + j_sum[i-1][j] - j_sum[i-1][j-1] + j_sum[i][j]
        o_sum[i][j] = o_sum[i][j-1] + o_sum[i-1][j] - o_sum[i-1][j-1] + o_sum[i][j]
        i_sum[i][j] = i_sum[i][j-1] + i_sum[i-1][j] - i_sum[i-1][j-1] + i_sum[i][j]

# 구간 합 출력하기
for _ in range(K):
    a, b, c, d = map(int, input().split())
    # 큰 범위에서 작은 범위 전까지의 합을 빼주고 중복된 부분 더해주기
    print(j_sum[c][d] - j_sum[c][b-1] - j_sum[a-1][d] + j_sum[a-1][b-1], end=' ')
    print(o_sum[c][d] - o_sum[c][b-1] - o_sum[a-1][d] + o_sum[a-1][b-1], end=' ')
    print(i_sum[c][d] - i_sum[c][b-1] - i_sum[a-1][d] + i_sum[a-1][b-1])
