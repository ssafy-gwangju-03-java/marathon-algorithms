# 원생 N명, 조 K개
N, K = map(int, input().split())

# 키 N개 / sorted
height = list(map(int, input().split()))

# 조별 비용 = 최장신 키 - 최단신 키
# 최소화하려면? => 인접 키차이 계산 , 이걸 정렬. 가장 큰 키 차이들 중에서 N-K개의 차이 골라서 합
#     => 큰 차이를 기준으로 조를 나누면 각 조 내의 키 차이는 줄어들게 되고, 따라서 비용도 줄어든다는 것!!!
# 전체 키 합에서 마지막에 선택한 합을 빼기
#     => 키차이 큰 것부터 N-K개 선택해서 조를 갈라버리자. 비용 회피
#     => 남는 차이는 결국 어느 조에 들어가든 키차이로 비용에 들어가게 될 것
height_diff = []
for i in range(1, N):
    height_diff.append(height[i] - height[i - 1])  # 인접키차이
height_diff.sort()  # 키차이 정렬
# print(height_diff)

print(sum(height_diff[:N - K]))  # N개에서 K개 뺴고 남는 키차이의 합이 비용임
