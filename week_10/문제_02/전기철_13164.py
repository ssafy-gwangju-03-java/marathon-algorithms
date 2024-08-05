# 13164 행복유치원
n, k = map(int, input().split())
lst = list(map(int, input().split()))
line = []

for i in range(n - 1):
    line.append(lst[i + 1] - lst[i]) # 옆칸과 차이값 저장
    
# print(line)
line.sort()
# print(line)

# 차이값 저장후 k값에 따라 큰거부터 하나씩 쳐내주면 됨 (그 사이에 팀을 나누는 벽을 세운다고 생각)
# if k==2면 sort 전 line=[2,2,1,4] , sort후 line=[1,2,2,4]이고 4를 쳐내면 됨 -> 차이가 4인 두 값 사이에 벽을 침 
# -> (1,3,5,6) / (10) -> 값 = 2+2+1 = 5
# if k==3 -> 차이가 4, 2인 영역 하나씩 벽치기
# -> (1,3)/(5,6)/(10) -> 2+1 = 3

ans = 0
for i in range(n - k):
    ans += line[i]
print(ans)
