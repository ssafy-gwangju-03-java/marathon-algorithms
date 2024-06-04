# 줄어드는 수

# 임시 리스트
down_lst = []
# 최종 줄어드는 수 리스트
result_lst = []

def dfs():
    if down_lst:
        result_lst.append(int(''.join(map(str, down_lst))))

    for i in range(10):
        if not down_lst or down_lst[-1] > i:
            down_lst.append(i)
            dfs()
            down_lst.pop()

N = int(input())

dfs()
result_lst.sort()

if N > len(result_lst):
    print(-1)
else:
    print(result_lst[N - 1])