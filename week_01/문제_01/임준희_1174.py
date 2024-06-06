from itertools import combinations

n = int(input())

# 줄어드는 수를 저장할 리스트
arr = []

# 1~10자리까지 줄어드는 수 생성
for i in range(1, 11):
    # 0부터 9까지 숫자 중 i개를 뽑는 모든 조합 생성
    for j in combinations(range(10), i):
        # 조합을 내림차순으로 정렬하고 문자열로 변환한 후 정수로 변환
        tmp = int("".join(map(str, sorted(j, reverse=True))))
        # 생성된 수 배열에 추가
        arr.append(tmp)

# 조합된 숫자들 다시 오름차순으로 정렬
arr.sort()

# n번째 숫자 출력 인덱스 0부터 시작하니까 n-1
if len(arr) > n-1:
    print(arr[n-1])
else:
    # n번째 수가 없으면 -1 출력
    print(-1)