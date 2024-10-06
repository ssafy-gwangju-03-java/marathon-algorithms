# 17404 RGB거리 2

n=int(input())
lst=[list(map(int,input().split()))for _ in range(n)]
ans=1000*1000+1

for i in range(3):
    chk=[[1000*1000+1]*3 for _ in range(n)]
    chk[0][i]=lst[0][i]
    for j in range(1,n):
        chk[j][0]=min(chk[j-1][1],chk[j-1][2])+lst[j][0]
        chk[j][1]=min(chk[j-1][0],chk[j-1][2])+lst[j][1]
        chk[j][2]=min(chk[j-1][0],chk[j-1][1])+lst[j][2]
    
    # 첫집과 마지막집이 같으면 안됨
    for k in range(3):
        if k==i:
            continue
        ans=min(ans,chk[n-1][k])
print(ans)