import sys
import heapq

sys.stdin = open("../../input.txt")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 과목별 우선순위 큐 초기화
pq = [[] for _ in range(3)]
grades = [[0] * N for _ in range(3)]

# 각 과목별 점수에 대해 최대 힙을 사용하여 순위 계산
for i in range(3):
    for j in range(N):
        heapq.heappush(pq[i], (-arr[i][j], j))

    last_score = -1
    last_grade = 1
    for j in range(N):
        score, participant = heapq.heappop(pq[i])
        if last_score == score:
            grades[i][participant] = last_grade
        else:
            grades[i][participant] = j + 1
            last_grade = j + 1
            last_score = score

for grade in grades:
    print(*grade)

scores = list(zip(arr[0], arr[1], arr[2]))
sum_scores = []
total_grades = [0] * N
for i in range(N):
    heapq.heappush(sum_scores, (-sum(scores[i]), i))

last_score = -1
last_grade = 1
for i in range(N):
    score, participant = heapq.heappop(sum_scores)
    if last_score == score:
        total_grades[participant] = last_grade
    else:
        total_grades[participant] = i + 1
        last_grade = i + 1
        last_score = score

print(*total_grades)
