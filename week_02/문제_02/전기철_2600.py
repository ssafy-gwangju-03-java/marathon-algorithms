# b1,b2,b3=map(int,input().split())
ball=list(map(int,input().split()))

# 미리 모든 경우의수 처리 해놓고 나중에 입력받아서 출력 진행

dp=[[0]*501 for _ in range(501)]

for i in range(501):
    for j in range(501):
        # dp[i][j]=1 -> A가 승리 else -> B 승리

        for k in range(3): # 왼쪽 통 구슬 꺼내기
            if i>=ball[k] and not dp[i-ball[k]][j]:
                dp[i][j]=1
                break

        for k in range(3): # 오른쪽 통
            if j>=ball[k] and not dp[i][j-ball[k]]:
                dp[i][j]=1
                break

for _ in range(5):
    k1,k2=map(int,input().split())
    if dp[k1][k2]:
        print('A')
    else:
        print('B')