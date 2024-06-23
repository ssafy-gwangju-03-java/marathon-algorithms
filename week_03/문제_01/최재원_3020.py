import sys
sys.stdin = open("../input.txt")

N, H = map(int, input().split())

# 높이 카운팅 배열
top = [0] * (H + 1)
bottom = [0] * (H + 1)

for i in range(N):
    height = int(input())

    if i % 2 == 0:
        top[height] += 1
    else:
        bottom[height] += 1


# 누적 개수 저장
for i in range(H - 1, 0, -1):
    top[i] += top[i + 1]
    bottom[i] += bottom[i + 1]

min_value = 200000
cnt = 0

for i in range(1, H + 1):
    current = top[i] + bottom[H - i + 1]

    if min_value > current:
        min_value = current
        cnt = 1
    elif min_value == current:
        cnt += 1

print(min_value, cnt)
