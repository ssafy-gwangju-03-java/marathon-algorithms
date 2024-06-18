# 개똥벌레

'''
input
6 7
1
5
3
3
5
1

output
2 3
'''
N, H = map(int, input().split())

cave = [int(input()) for _ in range(N)]

broke_lst = [0] * H

for i in range(N):
    if i % 2 == 0:
        # 아래에서부터 장애물을 추가
        broke_lst[0] += 1
        broke_lst[cave[i]] -= 1
    
    else:
        # 위에서부터 장애물을 추가
        broke_lst[H - cave[i]] += 1
    
# 누적합
for i in range(1, H):
    broke_lst[i] += broke_lst[i - 1]

# print(broke_lst)

min_broke = min(broke_lst)
print(min_broke, broke_lst.count(min_broke))