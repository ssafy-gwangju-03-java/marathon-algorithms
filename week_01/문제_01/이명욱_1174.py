# B1174 줄어드는 수

# 문제 요약
# 줄어드는 수 = 왼쪽부터 자리수가 감소할 때의 수
# N번째의 줄어드는 수 찾기

# N의 범위를 완전탐색하는 수의 범위로 착각한 점
# 시간복잡도 미고려한 점
# 문제 출처 참고 후(반복문 사용 -> 백트래킹 사용)

# 임시 리스트(줄어드는 수 만들기)
temp_lst = []
# 줄어드는 수 리스트
lst = []

# 백트래킹
def dfs():
    # 줄어드는 수가 만들어지면 리스트 삽입
    if temp_lst:
        # temp_lst에 삽입된 숫자들을 하나의 수로 만들어서 삽입
        lst.append(int("".join(map(str, temp_lst))))

    # 0 ~ 9 까지의 숫자 중 하나 선택
    for i in range(0, 10):
        # temp_lst가 비어있다면 어떤 숫자든 삽입 가능
        # or 줄어드는 수 만들기 위해 temp_lst의 마지막 수보다 작은 수 삽입
        if len(temp_lst) == 0 or i < temp_lst[-1]:
            temp_lst.append(i)
            dfs()
            temp_lst.pop()

# 찾아야하는 N번째 줄어드는 수 입력 받기
N = int(input())
dfs()
# 오름차순 정렬
lst = sorted(lst)

# 줄어드는 수 리스트의 길이 + 1 보다 N이 작으면 인덱스 고려하여 lst[N-1] 출력
# X번째 줄어드는 수 -> lst[X-1] 이니까 리스트 길이까지 N 범위 가능!!(제출-오답 이유)
if N < len(lst) + 1:
    print(lst[N - 1])
# 줄어드는 수 리스트의 길이 + 1 보다 N이 크면 없다는 것이므로 -1 출력
else:
    print(-1)

