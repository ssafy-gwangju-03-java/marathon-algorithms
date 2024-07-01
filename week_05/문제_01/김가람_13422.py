import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    house = list(map(int, sys.stdin.readline().split()))

    # 88% 오답
    if N == M:
        print(int(sum(house) < K))
        continue

    # M개 원소의 합을 저장할 배열
    sum_of_M_elem = [0] * N
    sum_of_M_elem[0] = sum(house[0 : M])

    """
    sum_of_M_elem[1] 
    = house[1] + house[2] + house[3]
    = sum_of_M_elem[0] + house[3] - house[0]
    ...
    sum_of_M_elem[N - 1] = house[N - 1] + house[0] + house[1]
    """

    for i in range(1, N):
        sum_of_M_elem[i] = sum_of_M_elem[i - 1] + house[(i + M - 1) % N] - house[i - 1]

    answer = 0
    for i in range(N):
        if sum_of_M_elem[i] < K:
            answer += 1

    print(answer)
