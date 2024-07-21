N = int(input())

# 양수, 음수(+ 0), 1 나눠서 리스트 받기
plus_lst = []
minus_lst = []
one_lst = []
ans = 0

for i in range(N):
    a = int(input())
    # 양수인경우
    if a > 1:
        plus_lst.append(a)
    # 양수, 0 인 경우(0은 음수와 곱해질 때 최대값 만들기 유리)
    elif a <= 0:
        minus_lst.append(a)
    # 1 인 경우
    else:
        one_lst.append(a)
plus_lst.sort(reverse=True)
minus_lst.sort()

# plus_lst의 길이가 홀수일 때 마지막 수(제일 작은 수) 더하기
if len(plus_lst) % 2 == 1:
    ans += plus_lst[len(plus_lst) - 1]
    # 앞에서부터 2개씩 짝지어 곱해서 더하기
    for i in range(0, len(plus_lst) - 1, 2):
        ans += (plus_lst[i] * plus_lst[i + 1])
# plus_lst의 길이가 짝수일 때 앞에서 부터 짝 지어 주기
else:
    for i in range(0, len(plus_lst), 2):
        ans += (plus_lst[i] * plus_lst[i + 1])

# 음수 계산
if len(minus_lst) % 2 == 1:
    # 홀수 일경우 마지막 수(제일 큰 값) 더하기
    ans += minus_lst[len(minus_lst) - 1] \
    # 앞에서부터 2개씩 짝지어 곱해서 더하기
    for i in range(0, len(minus_lst)-1, 2):
        ans += (minus_lst[i] * minus_lst[i + 1])
# minus_lst의 길이가 짝수일 때 앞에서 부터 짝 지어 주기
else:
    for i in range(0, len(minus_lst), 2):
        ans += (minus_lst[i] * minus_lst[i + 1])

# 1 에 대한 계산
if one_lst:
    ans += sum(one_lst)

print(ans)

# 틀린거 분기 잘못 나눔
# N = int(input())
#
# lst = [0] * N
# sm = 0
# for i in range(N):
#     a = int(input())
#     lst[i] = a
#     sm += a
#
# lst.sort(reverse=True)
#
# # print(lst)
#
# if N == 1:
#     print(sm)
# else:
#     i = 0
#     result = 0
#     while i <= N-2:
#         if lst[i] > 0 and lst[i + 1] > 0:
#             result += (lst[i] * lst[i + 1])
#             i += 2
#         elif lst[i] > 0 and lst[i + 1] == 0:
#             result += lst[i]
#             i += 1
#         elif lst[i] == 0 and lst[i + 1] < 0:
#             result += (lst[i] * lst[i + 1])
#             i += 2
#         elif lst[i] > 0 and lst[i + 1] < 0:
#             result += (lst[i] + lst[i + 1])
#             i += 2
#         elif lst[i] < 0 and lst[i + 1] < 0:
#             result += (lst[i] * lst[i + 1])
#             i += 2
#     print(max(sm, result))