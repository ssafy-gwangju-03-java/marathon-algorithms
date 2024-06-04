# https://www.acmicpc.net/problem/1174

import sys

input = sys.stdin.readline

# N번째로 작은 줄어드는 수 구하기
# 왜 50만번째 수는 없을까?
# -> 모든 자리수의 숫자가 줄어들어야 하기 때문에 가장 큰 줄어드는 수는 9876543210
#    총 개수가 50만개 미만일 수도 있다

N = int(input())
N -= 1  # 인덱스 변환

shrink_temp, shrink_list = [], []


def shrink_finder():
    if shrink_temp:
        # 재귀 진입 시 가져온 임시 리스트를 숫자로 변환 후 최종 리스트에 푸시
        shrink_list.append(int("".join(map(str, shrink_temp))))

    # 0~9까지 숫자 대입
    for i in range(10):
        # 임시 리스트가 비었거나 임시 리스트의 마지막 숫자가 i보다 작다면
        if not shrink_temp or shrink_temp[-1] > i:
            # 임시 리스트에 푸시
            shrink_temp.append(i)
            # 재귀 진입하여 다음 숫자 붙여보기
            shrink_finder()
            # 더 이상 붙일 숫자가 없어 재귀가 끝나면 마지막 숫자를 지우고 다음 숫자를 푸시
            shrink_temp.pop()


shrink_finder()
shrink_list.sort()

if N >= len(shrink_list):
    print(-1)
else:
    print(shrink_list[N])
