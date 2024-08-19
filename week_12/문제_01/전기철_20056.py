# 20056 마법사 상어와 파이어볼

dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]

def move():
    global lst
    arr=[[[] for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            for ball in lst[y][x]:
                m,s,d=ball
                nx=(x+dx[d]*s)%n
                ny=(y+dy[d]*s)%n
                arr[ny][nx].append([m,s,d]) # 이동 후 그 위치에 m s d 저장
    lst=arr # 다시 복사 
def boom():
    global lst
    arr = [[[] for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if len(lst[y][x])>=2: # 두개 이상 겹치는 경우
                cnt=len(lst[y][x]) # 볼 개수
                mass_sum=0
                speed_sum=0
                sum_d=[0,0] # 홀 짝 기록
                for ball in lst[y][x]:
                    mass_sum+=ball[0]
                    speed_sum+=ball[1]
                    sum_d[ball[2]%2]=1
                boom_mass=mass_sum//5
                boom_speed=speed_sum//cnt
                if sum(sum_d)==2: # 짝 홀 둘다 들어간 경우
                    dir=[1,3,5,7]
                else:
                    dir=[0,2,4,6]

                for d in dir:
                    if boom_mass:
                        arr[y][x].append([boom_mass,boom_speed,d])
            else:
                arr[y][x]=lst[y][x]
    lst=arr


def mass():
    ans=0
    for y in range(n):
        for x in range(n):
            for ball in lst[y][x]:
                ans+=ball[0]
    return ans

n,m,k=map(int,input().split())
lst=[[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,m,s,d=map(int,input().split())
    r-=1
    c-=1
    lst[r][c].append([m,s,d]) # (r,c) 좌표에 m,s,d 저장

for _ in range(k):
    move()
    boom()
print(mass())