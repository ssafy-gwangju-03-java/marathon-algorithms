# N: 물품의 개수, K: 준서가 버틸 수 있는 무게
N, K = map(int, input().split())

lst = []

for _ in range(N):
    # W: 물품 무게, V: 물품 가치
    W, V = map(int, input().split())
    lst.append((W, V))

dp = [0] * (K + 1)

for i in range(N):
    W, V = lst[i]
    # 무게 W ~ K 까지 확인
    for j in range(K, W - 1, -1):
        # 물품 추가 했을 때 가치가 크면 dp 값 갱신
        dp[j] = max(dp[j], dp[j-W] + V)

# 준서가 버틸 수 있는 무게
print(dp[-1])