N, S = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
sm = 0
min_v = 1e9

while True:
    # 합계가 S를 넘어가면 left 1씩 증가시키면서 짧은 길이 찾기
    if sm >= S:
        # 짧은 길이 비교 후 갱신
        min_v = min(min_v, right-left)
        sm -= lst[left]
        left += 1
    # 탈출 조건 right가 N일때
    elif right == N:
        break
    # right 1씩 증가하며 리스트의 값 더해주기
    else:
        sm += lst[right]
        right += 1

# 짧은 길이가 갱신 되지 않으면 0 출력
if min_v == 1e9:
    print(0)
else:
    print(min_v)