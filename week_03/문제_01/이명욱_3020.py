# 개똥벌레

N, H = map(int, input().split())

# 석순
down = [0] * (H + 1)
# 종유석
up = [0] * (H + 1)

for i in range(N):
    # 장애물의 길이
    m = int(input())
    # 석순
    if i % 2 == 0:
        down[m] += 1
    # 종유석
    else:
        up[m] += 1

# down[5] = 1 이라면 down[:5]의 장애물 하나씩 추가
for i in range(H - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

# 파괴해야 하는 장애물의 최소값 비교 위한 변수 할당
# 길이가 N이니까 부딪칠 수 있는 장애물의 최대값 N
min_b = N
# 최소값이 나타나는 구간의 수
min_b_count = 0

for i in range(1, H + 1):
    # 종유석은 아래서부터 석순은 위에서부터
    cnt = down[i] + up[H - i + 1]
    # 최소값 비교
    if min_b > cnt:
        min_b = cnt
        min_b_count = 1
    # 최소값 같을 경우 구간의 수 + 1
    elif min_b == cnt:
        min_b_count += 1

print(min_b, min_b_count)