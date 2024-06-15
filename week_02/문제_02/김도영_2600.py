# 구슬 게임

'''
input
1 3 4
4 1
5 5
10 2
15 16
30 14

output
A
B
A
A
B
'''

b_lst = list(map(int, input().split()))

for _ in range(5):
    k1, k2 = map(int, input().split())

    # dp 초기화
    # True이면 A가 이김
    # False이면 B가 이김
    dp = [[False] * (k2 + 1) for _ in range(k1 + 1)]

    dp[0][0] = False

    for i in range(k1 + 1):
        for j in range(k2 + 1):
            # 위에서 이미 처리
            if i == 0 and j == 0:
                continue

            # A를 기준으로 이길 수 있는지 없는지 확인
            win = False
            for b in b_lst:
                # k1 주머니에서 뺄 때
                # i >= b -> 뺄 수 있는 공의 갯수가 주머니 속에 있는 공의 갯수보다 적을 때
                # dp[i - b][j] == False -> k1 주머니에서 b개를 꺼냈을 때 상대가 지는 경우
                if i >= b and dp[i - b][j] == False:
                    win = True
                    break
                    
                # k2 주머니에서 뺄 때
                if j >= b and dp[i][j - b] == False:
                    win = True
                    break

            dp[i][j] = win

    if dp[k1][k2] == True:
        print('A')
    else:
        print('B')
            