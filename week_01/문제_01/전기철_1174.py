n = int(input())

lst = [] # 줄어드는 수 저장 리스트
down = [] # 임시 숫자 저장 리스트


def dfs():
    if down:
        lst.append(int("".join(map(str, down))))  # 리스트에 넣기

    for i in range(9, -1, -1):
        if not down or down[-1] > i:
            down.append(i)
            dfs()
            down.pop()


dfs()
lst.sort()

#print(lst)

if len(lst) + 1 > n:
    print(lst[n - 1])
else:
    print(-1)
