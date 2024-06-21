n=int(input())
x=[0]*100001
y=[0]*100001
garo=[0]*1000001
sero=[0]*1000001
garo_x=-500001
sero_y=-500001
garo_cnt=0
sero_cnt=0

for i in range(n):
    x[i],y[i]=map(int,input().split())


for i in range(n-1):
    if x[i]==x[i+1]: # 가로축 진행(가로선) -> 시작지점에선 +1, 끝지점에선 -1을 하는 방식을 통해 선분 영역에서만 교차횟수를 셀 수 있도록 세팅
        sero[max(y[i],y[i+1])+500000]-=1
        sero[min(y[i],y[i+1])+500000]+=1
    elif y[i]==y[i+1]:
        garo[max(x[i],x[i+1])+500000]-=1
        garo[min(x[i],x[i+1])+500000]+=1

if x[0]==x[n-1]: # 마지막점과 첫점을 이은 선이 가로선
    sero[max(y[0],y[n-1])+500000]-=1
    sero[min(y[0],y[n-1])+500000]+=1
elif y[0]==y[n-1]:
    garo[max(x[0],x[n-1])+500000]-=1
    garo[min(x[0],x[n-1])+500000]+=1

###################### 위 과정까지 진행했을 때 진행방향에 따른 증감치가 리스트에 나옴 
# ex2) 세로 -> 2, 0, 0, 0, 0, -2
#      가로 -> 4, 2, -2, -4
# print(garo[499990:500010])
# print(sero[499990:500010])

for i in range(1000001): # 위 리스트를 누적합 방식으로 변환하여 교차횟수로 변환
    sero_cnt+=sero[i] 
    sero[i]=sero_cnt
    sero_y=max(sero[i],sero_y)
    garo_cnt+=garo[i]
    garo[i]=garo_cnt
    garo_x=max(garo[i],garo_x)

# ex2) 세로 -> 2, 2, 2, 2, 2, 0
#      가로 -> 4, 6, 4, 0
# print(garo[499990:500010])
# print(sero[499990:500010])

print(max(garo_x,sero_y))
