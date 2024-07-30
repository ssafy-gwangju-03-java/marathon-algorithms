# 1806 부분합

# 풀이 방법 -> start를 고정값으로 두고 end를 끝까지 돌리면서 누적합 탐색 -> for문으로 start를 끝까지 보내면서 반복

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 0
sum = 0
cnt = 100001  # 개수 셀 변수

for start in range(n):
    while sum < m and end < n:
        sum += lst[end]
        end += 1

    if sum >= m:  # 조건에 맞으면
        cnt = min(cnt, end - start)  # cnt 갱신
        # 마지막에 end+=1했으므로 end-(start-1)-1 -> end-start
    sum -= lst[start]  # 처음 start값은 다 썼으니 뺴주기

if cnt == 100001:  # 조건에 맞은적이 없음 -> 불가능
    print(0)
else:
    print(cnt)
