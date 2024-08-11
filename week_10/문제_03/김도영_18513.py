from collections import deque

N, K = map(int, input().split())
sam = list(map(int, input().split()))

q = deque()

# 초기 샘터 위치를 큐에 넣고 방문 처리
for i in range(N):
    q.append((sam[i], 0))

# 샘터의 위치를 방문한 곳으로 처리
vis = set(sam)

# 현재까지 지은 집의 갯수
cnt = 0
# 총 불행도
result = 0

while q:
    now, distance = q.popleft()
    
    for i in [-1, 1]:
        # 양 옆 탐색
        ni = now + i
        # 방문하지 않았던 곳이면
        if ni not in vis:
            q.append((ni, distance + 1))
            vis.add(ni)
            cnt += 1
            result += distance + 1
        
        if cnt == K:
            break
    
    if cnt == K:
        break

print(result)
