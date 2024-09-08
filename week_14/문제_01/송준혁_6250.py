# https://softeer.ai/practice/6250

## Referenced
# https://stritegdc.tistory.com/353

import sys

input = sys.stdin.readline

N = int(input())
# 대회 점수 및 최종 점수 합 저장 배열
contest = [[] for _ in range(4)]
# 대회별 순위 저장 배열
contest_rank = [[0] * N for _ in range(4)]

# 대회 점수를 받은 후 각 점수와 인덱스 저장
for i in range(3):
    scores = list(map(int, input().split()))
    for idx, score in enumerate(scores):
        contest[i].append([idx, score])

# 각 인덱스별 대회 점수 합산 후 최종 점수 저장
for i in range(N):
    score_sum = sum(contest[j][i][1] for j in range(3))
    contest[-1].append([i, score_sum])

# 각 점수별 내림차순 정렬
for c in contest:
    c.sort(key=lambda x: x[1], reverse=True)

# 대회 순위 설정
for i in range(4):
    count = 1
    rank = 1
    # i번 대회의 첫 번째의 인덱스를 인덱스로 하여 순위 배열에 저장
    contest_rank[i][contest[i][0][0]] = rank
    for j in range(1, N):
        # j 인덱스의 점수가 j-1 인덱스와 같다면 동일 순위 설정
        if contest[i][j - 1][1] == contest[i][j][1]:
            contest_rank[i][contest[i][j][0]] = rank
            count += 1
        # 점수가 다르다면 다음 순위로 설정
        else:
            rank += count
            contest_rank[i][contest[i][j][0]] = rank
            count = 1

for r in contest_rank:
    print(*r)
