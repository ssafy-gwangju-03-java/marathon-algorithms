# 물건 N개, 최대무게 K개,
N, K = map(int, input().split())
# 각 물건의 무게 W, 가치 V , 총 N개의 줄
things = [tuple(map(int, input().split())) for _ in range(N)]

# https://jeonyeohun.tistory.com/86

# bag[k][w] = 물건 번호 k, k번째 물건의 무게 w
bag = [[0] * (N + 1) for _ in range(W + 1)]
