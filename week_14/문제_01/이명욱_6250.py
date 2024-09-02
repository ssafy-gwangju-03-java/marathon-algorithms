# 등수 정하기
def find(dic, lst):
    idx = 0
    # 첫 번째 수는 무조건 1등
    dic[lst[0]] = 1
    # 연속된 수 카운트
    connect = 1
    # 뒤에서 두번째 인덱스까지
    while idx <= N - 2:
        # 내림차순한 리스트의 값이 같을 경우
        if lst[idx] == lst[idx + 1]:
            # 커넥트 1 증가
            connect += 1
        # 같지 않을 경우
        else:
            # 직전 큰 수의 등수에 connect 만큼 더해주기
            # 직전에 연속된 수가 없으면 connect( = 1) 만큼 더해주기
            dic[lst[idx + 1]] = dic[lst[idx]] + connect
            # connect 초기화
            connect = 1
        # 인덱스 1 증가
        idx += 1
    return dic


# 등수 출력하기
# 원래 리스트 순회하면서 리스트 값을 키로 딕셔너리 값 출력
def output(dic, lst):
    for i in range(N):
        print(dic[lst[i]], end=" ")


N = int(input())

# 점수 입력 받기
first_lst = list(map(int, input().split()))
second_lst = list(map(int, input().split()))
third_lst = list(map(int, input().split()))

# 내림차순 정렬
r_first_lst = sorted(first_lst, reverse=True)
r_second_lst = sorted(second_lst, reverse=True)
r_third_lst = sorted(third_lst, reverse=True)

# 합계 점수
total_lst = [0] * N
for i in range(N):
    total_lst[i] = first_lst[i] + second_lst[i] + third_lst[i]

# 합계 점수 내림 차순 정렬
r_total_lst = sorted(total_lst, reverse=True)

# 등수 정한 다음 받을 딕셔너리
first = find(dict(), r_first_lst)
second = find(dict(), r_second_lst)
third = find(dict(), r_third_lst)
total = find(dict(), r_total_lst)

# 결과 출력
output(first, first_lst)
print()
output(second, second_lst)
print()
output(third, third_lst)
print()
output(total, total_lst)