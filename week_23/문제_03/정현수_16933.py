from collections import deque
import sys

n, m, k = map(int, input().split())
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
d = deque([(0, 0, 0, 1)]) # k, n, m, 현재까지의 거리
visited[0][0][0] = 1

while d:
  ck, cn, cm, dist = d.popleft()  # dist : 밤/낮 정보이자 거리정보
  # 도착
  if cn == n - 1 and cm == m - 1:
    print(dist)
    break

  day = dist % 2  # dist가 짝수면 밤
  for dn, dm in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    nn, nm = cn + dn, cm + dm
    if (0 <= nn < n and 0 <= nm < m):
      # 일반 탐색
      if visited[ck][nn][nm] == 0 and graph[nn][nm] == 0:
        visited[ck][nn][nm] = dist
        d.append((ck, nn, nm, dist + 1))

      # 첫 방문인 벽 부수기
      elif (ck < k and graph[nn][nm] == 1 and visited[ck + 1][nn][nm] == 0):
        # 낮이라면
        if day:
          visited[ck + 1][nn][nm] = dist
          d.append((ck + 1, nn, nm, dist + 1))
        # 밤이라면
        else:
          d.append((ck, cn, cm, dist + 1)) # 하루 대기

else:
  print(-1)