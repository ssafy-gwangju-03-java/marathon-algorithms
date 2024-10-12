#5972 택배 배송


import heapq

n,m=map(int,input().split())

lst=[[] for _ in range(n+1)]

# 양방향 길
for _ in range(m):
    a,b,c=map(int,input().split())
    lst[a].append((c,b))
    lst[b].append((c,a))

INF=1e9
dis=[INF]*(n+1)
q=[[0,1]] #비용, 출발점

while q:
    cost,now=heapq.heappop(q)
    for nxt_cost,next in lst[now]:
        if cost+nxt_cost<dis[next]:
            new_cost=nxt_cost+cost
            dis[next]=new_cost
            heapq.heappush(q,(new_cost,next))

print(dis[n])
            

