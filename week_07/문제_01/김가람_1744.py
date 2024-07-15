import sys
import heapq

N = int(sys.stdin.readline())


# 1을 제외한 양수와 음수는 따로 관리
negative = []
positive = []

# 0은 음수와 곱해주면 이득이라서 따로 분리해놓음
zero = 0

# 1은 다른 수와 곱해봤자 전혀 이득이 없어서 그냥 더해줘야하기 때문에 분리해놓음
one = 0


# 분리해서 입력
# 자동정렬 위해 heap 사용
for _ in range(N):
    num = int(sys.stdin.readline())
    if num < 0:
        heapq.heappush(negative, num)
    elif num == 0:
        zero += 1
    elif num == 1:
        one += 1
    else:
        heapq.heappush(positive, num * -1)


total = 0

# 음수 처리
# 음수가 짝수개로 존재하면 절댓값이 큰 순서부터 묶어서 곱한 후 더해주면 이득
while len(negative) > 1:
    total += heapq.heappop(negative) * heapq.heappop(negative)
# 음수가 1개만 존재하면 0과 곱해주거나, 0이 없을 시 그냥 더해준다 (양수와 곱하면 손해)
if negative:
    if zero:
        zero -= 1
    else:
        total += heapq.heappop(negative)


# 양수 처리
# 양수가 2개 이상 존재하면 큰 순서부터 묶어서 더해주고 남은 하나는 그냥 더해줌
while len(positive) > 1:
    total += heapq.heappop(positive) * heapq.heappop(positive)
# 양수가 1개만 존재하면 그냥 더해주는 것이 이득
if positive:
    # -1 곱해준 이유: heappop하려고 최대힙으로 설정함
    total += heapq.heappop(positive) * -1


# 1은 그냥 더해주는게 이득
if one:
    total += one

print(total)
