# from math import comb # 이건 조합의 경우의 수만 계산해줌
from itertools import combinations

N = int(input())

# N번째로 작은 줄어드는 수 출력, 없으면 -1
# 예제 3에 50만번째 작은 수는 왜 없지?? 수의 범위가 유한한가?
# 줄어드는 수는 최대 9876543210까지 있으니까 유한한 게 맞음
# 조합으로 1개 ~ 10개 고르기까지 하고
# 각 경우마다 고르고 나면, 큰 수부터 정렬, 문자로 바꿔서 더해주고 다시 숫자로 변환
# 이걸 답 배열에 푸시
# 이걸 각 조합마다 반족, 대신 해당조합이 답 배열에 없을때만 시행하기!
# 근데 조합 library가 있넴 >>> 이걸 쓰니까 훨씬 간편하게 풀림 !!!

# print(list(combinations(range(9), 2)))
ans = []

for cnt in range(1, 11):  # 1~10개 고를 것이다
    # 0~9로 조합을 만들 것이다. 고르는 개수는 cnt개.
    for comb in combinations(range(10), cnt):
        # comb = list(comb).sort(reverse=True)
        comb = sorted(list(comb), reverse=True)
        # print(comb)
        ans.append(int(''.join(map(str, comb))))
# print(sorted(ans))
if N <= len(ans): # N-1 번 인덱스를 찾기 때문에 < 말고 <=로 해야 됨
    print(sorted(ans)[N - 1])
else:
    print(-1)