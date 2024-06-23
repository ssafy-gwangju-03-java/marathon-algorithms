import sys

N, H = map(int, sys.stdin.readline().split())

# i 번째 원소 == 높이가 i인 석순, 종유석의 갯수
ground = [0] * (H + 1)
ceiling = [0] * (H + 1)


# input() 쓰면 시간초과
for i in range(N):
    height = int(sys.stdin.readline())
    if i % 2 == 0:
        ground[height] += 1
    else:
        ceiling[height] += 1


# 누적합
# - 높이가 i인 석순에 부딪히면 i + 1번째 석순에도 당연히 부딪히게 됨
# - 높이가 1인 석순에 부딪히면 나머지 모든 석순에도 부딪히게 됨
for i in range(H - 1, 0, -1):
    ground[i] += ground[i + 1]
    ceiling[i] += ceiling[i + 1]


min_hit = 200001
cnt = 0

for i in range(1, H + 1):
    curr_hit = ground[i] + ceiling[H-i+1]
    if min_hit > curr_hit:
        min_hit = curr_hit
        cnt = 1
    elif min_hit == curr_hit:
        cnt += 1

print(min_hit, cnt)