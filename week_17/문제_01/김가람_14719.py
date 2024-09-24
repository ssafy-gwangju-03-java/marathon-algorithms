import sys

R, C = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))
water = 0

# 왼쪽부터 탐색
left = 0
for i in range(1, C):
    # 오른쪽에 자신(왼쪽)보다 크거나 같은 벽이 있다면 물이 고인대로 더해줌
    if block[left] <= block[i]:
        if block[left] != 0:    # 왼쪽이 0이 아니라면 (블럭이 있다면)
            for j in range(left + 1, i):
                water += block[left] - block[j]
        left = i    # 왼쪽 갱신

# 오른쪽부터 탐색
right = C - 1
for i in range(C - 2, -1, -1):
    # 왼쪽에 자신(오른쪽)보다 큰 벽이 있다면 물이 고인대로 더해줌 (같은 높이인 경우는 위의 왼쪽 방향 탐색에서 이미 탐색했으므로 제외)
    if block[right] < block[i]:
        if block[right] != 0:    # 오른쪽이 0이 아니라면 (블럭이 있다면)
            for j in range(right - 1, i, -1):
                water += block[right] - block[j]
        right = i   # 오른쪽 갱신

print(water)