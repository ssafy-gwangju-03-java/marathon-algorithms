from collections import deque

k = int(input().strip())
w, h = map(int, input().split())

# 말이 움직이는 방식
horse_mv = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
# 원숭이가 움직이는 방식
monkey_mv = [(-1, 0), (1, 0), (0, 1), (0, -1)]

board = [list(map(int, input().split())) for _ in range(h)]
# 나이트처럼 움직일 수 있는 횟수, 행, 열
visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]
q = deque([(0, 0, 0)])
# 목표지점 도착 여부
flag = 0
# 시작 지점
visited[0][0][0] = 1

while q:
  cnt, ch, cw = q.popleft()
  # 목표 도착
  if ch == h - 1 and cw == w - 1:
    # 시작 지점 이동 횟수 제외
    print(visited[cnt][ch][cw] - 1)
    flag = 1
    break

  # 원숭이처럼 이동
  for i, j in monkey_mv:
    nh, nw = ch + i, cw + j
    if (0 <= nh < h and 0 <= nw < w and board[nh][nw] != 1 and not visited[cnt][nh][nw]):
      visited[cnt][nh][nw] = visited[cnt][ch][cw] + 1
      q.append((cnt, nh, nw))

  # 말처럼 이동
  if cnt < k:
    for i, j in horse_mv:
      hh, hw = ch + i, cw + j
      if 0 <= hh < h and 0 <= hw < w and board[hh][hw] != 1:
        # 말처럼 움직인 횟수 증가 : 배열 차수 + 1
        if not visited[cnt + 1][hh][hw]:
          visited[cnt + 1][hh][hw] = visited[cnt][ch][cw] + 1
          q.append((cnt + 1, hh, hw))

if not flag:
  print(-1)