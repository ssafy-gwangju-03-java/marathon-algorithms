import sys
from heapq import heappush, heappop, heapify

N = int(sys.stdin.readline())

# 최종 등수 저장할 리스트
total_scores = [0] * N

def print_rank(max_heap_with_tuple):
    rank_list = [0] * N

    rank = 0  # 등수
    last_score = 0  # 직전에 heappop 된 사람의 점수
    same = 1  # 동점자 수

    for i in range(N):
        # (score == 큰 순서로 정렬된 점수, idx == idx 번째 사람)
        score, idx = heappop(max_heap_with_tuple)

        if last_score != score:
            # 동점자 수만큼 rank를 한꺼번에 올려주고 동점자 수는 초기화
            rank += same
            same = 1
        else:
            # 전 등수의 사람과 동점이면 same += 1
            same += 1

        # idx 번째 사람의 순위는 rank
        rank_list[idx] = rank
        last_score = score

    print(*rank_list)

for _ in range(3):
    score_hip = []
    scores = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        heappush(score_hip, (-1 * scores[i], i))  # 최대힙으로 만들기
        total_scores[i] += scores[i]

    print_rank(score_hip)

for i in range(N):
    total_scores[i] = (-1 * total_scores[i], i)

heapify(total_scores)
print_rank(total_scores)
