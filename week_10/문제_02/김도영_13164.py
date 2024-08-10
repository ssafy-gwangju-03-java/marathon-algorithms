# 행복 유치원

N, K = map(int, input().split())
height = list(map(int, input().split()))

diff_lst = []
length = N

for i in range(N - 1):
    diff_lst.append(height[i + 1] - height[i])
    length -= 1

diff_lst.sort()

result = sum(diff_lst[:N - K])
  
print(result)