# https://www.acmicpc.net/problem/3020

## Referenced
# https://github.com/ssafy-gwangju-03-java/marathon-algorithms/blob/main/week_03/문제_01/이정하_3020.py

import sys

input = sys.stdin.readline
N, H = map(int, input().split())
cave = [int(input()) for _ in range(N)]

# 특정 높이를 가진 장애물의 개수 저장 배열
block_a = [0] * (H + 1)  # 석순
block_b = [0] * (H + 1)  # 종유석

for i in range(N):
    # 짝수 인덱스 -> 석순
    if i % 2 == 0:
        block_a[cave[i]] += 1
    # 홀수 인덱스 -> 종유석
    else:
        """
        종유석은 중간에서부터 구간 계산에 걸리기 때문에
        구간 계산 시 걸리기 시작하는 높이를 저장
        ex) 높이 7, 종유석 5라면 높이 3부터 종유석에 걸림
        """
        block_b[H + 1 - cave[i]] += 1

# 겹치는 구간의 누적합 계산
for h in range(1, H + 1):
    # 석순: 높이가 낮아질수록 겹치는 구간이 증가
    block_a[H - h] += block_a[H - h + 1]
    # 종유석: 높이가 높아질수록 겹치는 구간이 증가
    block_b[h] += block_b[h - 1]

blocks, count = 1e9, 0
for h in range(1, H + 1):
    # 높이 h에서의 석순, 종유석의 누적 개수
    blocks_sum = block_a[h] + block_b[h]
    if blocks > blocks_sum:
        blocks = blocks_sum
        count = 1
    elif blocks == blocks_sum:
        count += 1

print(blocks, count)
