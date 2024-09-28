# 6250 성적 평가
import sys

input = sys.stdin.readline

n = int(input())
ans = [0] * n
for _ in range(3):
    lst = list(map(int, input().split()))
    for i in range(n):
        ans[i] += lst[i]
    scores = sorted(lst, reverse=True)
    dic = {}
    rank = 1
    cnt = 1
    for idx, score in enumerate(scores):
        if idx == 0:  # 처음은 그대로 저장
            dic[score] = rank
        else:
            if scores[idx - 1] == score:  # 크기 같음
                dic[score] = rank  # 이전 순위 그대로
                cnt += 1
            else:  # 다름
                rank += cnt  # 겹치는만큼 더해줌
                dic[score] = rank
                cnt = 1
    # print(dic)
    for i in range(n):
        print(dic[lst[i]], end=" ")
    print()
# 총점 리스트를 가지고 위 과정 한번 더 진행
rank = 1
cnt = 1
scores = sorted(ans, reverse=True)
dic = {}
# print(scores)
for idx, score in enumerate(scores):
    if idx == 0:
        dic[score] = rank
    else:
        if scores[idx - 1] == score:
            dic[score] = rank
            cnt += 1
        else:
            rank += cnt
            dic[score] = rank
            cnt = 1
for i in range(n):
    print(dic[ans[i]], end=" ")
print()
