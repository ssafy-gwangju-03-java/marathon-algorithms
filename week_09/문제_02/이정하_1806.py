# 최대 배열 크기를 정의
MAX_ARR = 100000


# 두 값 중 작은 값 리턴
def min(x, y):
    return x if x < y else y


N, S = map(int, input().split())

# 수열
arr = list(map(int, input().split()))

# 필요한 포인터, 변수
low = 0
high = 0
subsum = arr[0]
length = N + 1

# 1. 현재 부분합(low~high sum)이 S 보다 작은 경우
#  - high 를 오른쪽으로 한 칸 이동하고 sum 에 arr[high] 값을 더해준다.

# 2. 현재 부분합(low~high sum)이 S 보다 크거나 같은 경우
#  - 현재 len 값과 현재 부분합의 길이(high - low + 1)를 비교하여 작은 값을 len 에 기록한다.
#  - 다음 탐색을 위해 sum 에서 arr[low] 값을 빼주고 low 를 오른쪽으로 한 칸 이동한다.

while low <= high and high < N:
    # 반복 1) low 가 high 보다 작거나 같은 경우
    #  - 수열 중 1개의 숫자만으로 S 이상이 되면, 다음 반복 시 low 가 high 보다 커지게 됨
    #  - low 가 더 커진 경우 최소 길이는 1이고 더 이상 탐색할 이유가 없음=> 반복종료
    # 반복 2) high 가 N 보다 작은 경우
    #  - high 가 N 에 도달했다는 것은 현재 sum 이 S 보다 작은 상태로 끝까지 도달한 것
    #  - sum 을 더 크게 만들 수 있는 방법이 없음=>반복종료
    if subsum < S:
        # 현재 합이 s보다 작으면 high 포인터 이동
        high += 1
        if high < N:
            subsum += arr[high]
    else:
        # 현재 합이 s보다 크거나 같으면 길이 확인하고 최소 길이로 갱신
        length = min(length, high - low + 1)
        # low 포인터를 이동하여 윈도우 축소
        subsum -= arr[low]
        low += 1

# 유효한 부분 발견되지 않았으면 길이는 0
if length == N + 1:
    length = 0

print(length)
