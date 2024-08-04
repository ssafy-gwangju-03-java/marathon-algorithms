# https://www.acmicpc.net/problem/1806

## Referenced
# https://codinghejow.tistory.com/246

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
arr_sum = arr[0]
result = 1e9

while True:
    # 누적합이 S보다 작을 경우
    if arr_sum < S:
        # 끝 포인터가 배열을 넘어갔으면 종료
        if e + 1 == N:
            break
        # 아니라면 끝 포인터 증가 후 누적합에 추가
        else:
            e += 1
        arr_sum += arr[e]
    # 누적합이 S에 도달했을 경우
    else:
        # 길이 최소값 도출
        result = min(result, e - s + 1)
        # 앞 포인터가 s일 때의 누적합 최소 길이를 구했으므로
        # 누적합에서 앞 포인터의 값을 뺀 후 앞 포인터 이동
        arr_sum -= arr[s]
        s += 1

if result != 1e9:
    print(result)
else:
    print(0)
