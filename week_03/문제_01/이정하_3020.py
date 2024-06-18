# 누적합 버전
# 동굴 길이 N, 동굴 높이 H
N, H = map(int, input().split())

floor = [0] * (H + 1)
ceiling = [0] * (H + 1)

# 석순, 종유석 높이 개수를 각 배열에 저장하기
cave = [int(input()) for _ in range(N)]
for i in range(N):
    if i % 2 == 0:  # 석순
        floor[cave[i]] += 1
    else:  # 종유석
        ceiling[H + 1 - cave[i]] += 1

# 높이별 누적합 구하기
for h in range(1, H + 1):
    ceiling[h] += ceiling[h - 1]
    floor[H - h] += floor[H + 1 - h]

min_bar = N + 1  # 파괴한 장애물 개수 최솟값
cnt = 0  # 장애물 최솟값 구간 개수

# 높이별 파괴한 장애물 개수 계산하기
for h in range(1, H + 1):
    # 총 부술 장애물 개수
    total_barrier = floor[h] + ceiling[h]
    # 최솟값 갱신
    if total_barrier < min_bar:
        min_bar = total_barrier
        cnt = 1  # 최솟값 갱신하면 최소장애물 구간 개수 초기화
    elif total_barrier == min_bar:
        cnt += 1  # 구간 개수 갱신
print(min_bar, cnt)

'''
# 완탐 - 메모리초과
# 동굴 길이 N
# 동굴 높이 H
N, H = map(int, input().split())

cave = [[0 for _ in range(H)] for _ in range(N)]  # 옆으로 눕혔다...
# print(cave)

for r in range(N):
    now = int(input())
    # print('n', now)
    # for r in range(N):
    if r % 2 == 0:  # 짝수면 석순
        for c in range(now):
            cave[r][c] = 1
            # print(c,end=' ')
    else:  # 홀수면 종유석
        for c in range(H - 1, H - 1 - now, -1):
            cave[r][c] = 1
            # print(c,end=' ')
    # print('\n', cave)
# print(cave)

# 완탐밖에 모르겠는데.. 제한시간 보면 완탐하면 시간초과 나겠는데,,,
# 그래 일단 완탐으로 풀고 생각해보자
min_bar = N + 1  # 파괴한 장애물 개수 최솟값
cnt = 0  # 장애물 최솟값 구간 개수
for c in range(H):
    barrier = 0  # 파괴한 장애물 개수
    # print(min_bar)
    for r in range(N):
        if cave[r][c] == 1:
            # print(111111)
            barrier += 1
    # print('bar',barrier)
    # print('min bar',min_bar)
    if min_bar > barrier:
        min_bar = barrier
        # print('m',min_bar)
        cnt = 1  # 최솟값 이 갱신된거라 최솟값 구간 개수도 1부터 시작
    elif min_bar == barrier:
        # print(222)
        cnt += 1  # 장애물 최솟값 구간 개수
    # print(cnt)

print(min_bar, cnt)
'''
"""
# 이진탐색... 실패 ㅠ 
# 동굴 길이 N
# 동굴 높이 H
N, H = map(int, input().split())


# arr: 종유석 or석순
# height: 현재높이 h
# is_celing: 종유석 여부
def bin_search(arr, height, is_ceiling):
    '''
    :param arr: 정렬된 종유석 or 석순
    :param height: 현재 벌레 높이
    :param is_ceiling: 종유석 여부(종유석 True)
    :return:
    '''
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        # if is_ceiling:
        #     if arr[mid] < height:
        #         start = mid + 1
        #     else:
        #         end = mid
        # else:
        #     if arr[mid] <= height:
        #         start = mid + 1
        #     else:
        #         end = mid
        # -----
        # if arr[mid] < height if is_ceiling else arr[mid] <= height:
        #     start = mid + 1
        # else:
        #     end = mid
        if (is_ceiling and arr[mid] < height) or (not is_ceiling and arr[mid] <= height):
            start = mid + 1
        else:
            end = mid
    return start


cave = [int(input()) for _ in range(N)]
print(cave)
# 석순, 종유석 따로 저장하고 정렬하기
floor = sorted(cave[0::2])  # 석순(0부터 끝까지 2칸씩)
ceiling = sorted(cave[1::2])  # 종유석
print(floor)
print(ceiling)

min_bar = N + 1  # 파괴한 장애물 개수 최솟값
cnt = 0  # 장애물 최솟값 구간 개수

# 이진탐색 start , end
# 개똥벌레 높이 따라 부숴야 하는 장애물 수 계산하기
for h in range(1, H + 1):
    # 이진탐색으로 현재 높이 h에서 부숴야 하는 석순 종유석 개수 구하기
    # h 높이 이상 부숴야 하는 석순 수 계산
    floor_bar = len(floor) - bin_search(floor, h, False)
    # 종유석은 거꾸로 달려있음 => 높이가 H +1 - h
    ceiling_bar = len(ceiling) - bin_search(ceiling, H + 1 - h, True)

    # 총 부숴야 하는 장애물 개수
    total_barrier = floor_bar + ceiling_bar
    print('tb:', total_barrier, '/ floorbar: ', floor_bar, '/cb: ', ceiling_bar)
    # 파괴한 장애물 개수 최솟값 갱신하기
    if total_barrier < min_bar:
        print(111)
        min_bar = total_barrier
        cnt = 1
    elif total_barrier == min_bar:
        cnt += 1
        print(2222)
print(min_bar, cnt)
"""
