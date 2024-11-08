import sys
input = sys.stdin.readline

T = int(input())

# 자리수 별 최댓값
# 합   순서
# 1    1
# 2    1 1
# 4    1 2 1
# 6    1 2 2 1
# 9    1 2 3 2 1
# 12   1 2 3 3 2 1
# 16   1 2 3 4 3 2 1
# 20   1 2 3 4 4 3 2 1
# 25   1 2 3 4 5 4 3 2 1
#
# 간격 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8
# 가운데 1이 증가한 숫자를 두번씩 넣을 수 있다고 생각하자

for tc in range(1, T + 1):
    x, y = map(int, input().split())

    # 2번에 한번씩 숫자를 올릴 때 사용할 카운트
    count = 0
    # 더할 숫자
    add_num = 1
    # 거리
    distance = y - x

    # 현재까지 더한 값
    curr_sum = 0

    while True:
        if curr_sum >= distance:
            break

        curr_sum += add_num
        # 2번에 한 번 씩 1 늘려서 더하기
        if count % 2 == 1:
            add_num += 1

        count += 1

    print(count)

