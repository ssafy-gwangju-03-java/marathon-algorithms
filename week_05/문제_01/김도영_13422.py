# 도둑
'''
1
5 5 16
1 2 3 4 5
1
8 3 15
3 4 7 5 6 4 2 9
'''
T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    money_lst = list(map(int, input().split()))

    cnt = 0
    if N == M:
        if sum(money_lst) < K:
            cnt = 1
    
    elif M == 1:
        for idx in range(N):
            if money_lst[idx] < K:
                cnt += 1

    else:
        money = sum(money_lst[: M])
        if money < K:
            cnt += 1
        
        start = 0
        end = M
        for _ in range(N - 1):
            money -= money_lst[start % N]
            money += money_lst[end % N]
            start += 1
            end += 1

            if money < K:
                cnt += 1
    
    print(cnt)