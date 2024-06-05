# 명제 증명

N = int(input())

# 입력 받은 명제 리스트
check = [[0] * 58 for _ in range(58)]

cnt = 0
for _ in range(N):
    lst = list(input().split())
    if lst[0] != lst[2] and check[ord(lst[0]) - 65][ord(lst[2]) - 65] == 0:
        check[ord(lst[0]) - 65][ord(lst[2]) - 65] = 1
        cnt += 1

# i가 거쳐가는 노드
# j가 거쳐가는 노드인줄 알고 한참을 틀렸네....
for i in range(58):
    for j in range(58):
        for k in range(58):
            if check[j][i] == 1 and check[i][k] == 1 and j != k and check[j][k] == 0:
                check[j][k] = 1
                cnt += 1

print(cnt)
for i in range(58):
    for j in range(58):
        if check[i][j] == 1:
            print(f'{chr(i + 65)} => {chr(j + 65)}')