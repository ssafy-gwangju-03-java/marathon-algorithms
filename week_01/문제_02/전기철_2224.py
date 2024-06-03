n=int(input())
lst=[[0]*58 for _ in range(58)] # A가 65, z가 122 -> 58개
cnt=0 #명제 개수
for _ in range(n):
    line=str(input())
    if line[0]==line[5]: # 입력 중 a => a 이런게 있는거같아서 처리
        continue
    if not lst[ord(line[0])-65][ord(line[5])-65]: # 아직 연결처리를 안했으면
        lst[ord(line[0])-65][ord(line[5])-65]=1 # 연결처리
        cnt+=1 # 개수 증가

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i!=j and lst[i][k] and lst[k][j] and not lst[i][j]: # a->b / b->c 이런 케이스의 경우 a->c도 연결해줘야 함
                lst[i][j]=1
                cnt+=1

print(cnt)
for i in range(58):
    for j in range(58):
        if lst[i][j]:
            print(chr(i+65)+" => "+chr(j+65))