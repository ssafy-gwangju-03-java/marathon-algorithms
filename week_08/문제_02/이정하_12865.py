# 물건 N개, 최대무게 K개,
N, K = map(int, input().split())
# 각 물건의 무게 W, 가치 V , 총 N개의 줄
things = [tuple(map(int, input().split())) for _ in range(N)]

# https://jeonyeohun.tistory.com/86

# bag[k][w] = 물건 번호 k, k번째 물건의 무게 w
bag = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        # 물건의 무게가 현재 바낭의 무게보다 작거나 같으면
        if things[i - 1][0] <= w:
            # 물건을 넣는거/안넣는 거 중 가치가 더 높은 경우 고르기
            bag[i][w] = max(bag[i - 1][w], bag[i - 1][w - things[i - 1][0]] + things[i - 1][1])
        else:  # 물건 무게가 현재 배낭 무게보다 크면
            bag[i][w] = bag[i - 1][w]  # 안넣음

print(bag[N][K])
