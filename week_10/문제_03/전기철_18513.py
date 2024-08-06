# 18513 샘터
from collections import deque

dx = [-1, 1]
n, k = map(int, input().split())
sam = list(map(int, input().split()))
q = deque()
for i in range(n):
    q.append((sam[i], 1))
vis = set(sam)
# vis 배열을 미리 선언하니까 크기때문에 바로 메모리초과
# list로 하니까 탐색이 O(N)이라서 시간초과
cnt = 0
ans = 0
while q:
    now, dis = q.popleft()
    for i in range(2):
        if now + dx[i] not in vis:  # 양 옆 탐색, 방문x이면
            q.append((now + dx[i], dis + 1))  # q에 집 세운 지점과 거리 append
            vis.add(now + dx[i])  # 집 세운지점 방문처리
            cnt += 1
            ans += dis  # ans에 거리 더하기
        if cnt == k:
            break
    if cnt == k:
        break
print(ans)
