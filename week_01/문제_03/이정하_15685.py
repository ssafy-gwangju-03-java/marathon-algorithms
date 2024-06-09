# 1. 드래곤 커브 그리기
# 2. 정사각형 찾기


# 방향배열
# 0 1 2 3 우 상 좌 하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 100*100 좌표평면
# 좌표 범위 0 이상 100 이하
plane = [[0] * 101 for _ in range(101)]

N = int(input())  # 드래곤 커브 개수

# 드래곤커브 좌표 [c, r, 방향, 세대] 순서
data = [list(map(int, input().split())) for _ in range(N)]

# 1. 드래곤 커브 그리기
for i in range(N):
    r, c = data[i][1], data[i][0]
    d = data[i][2]
    gen = data[i][3]

    # 좌표 시작점을 평면에 표시하기
    plane[r][c] = 1

    # 각 시작점 별 커브 방향의 리스트
    # 이 회차의 리스트 완성하고 나서
    # 그 방향대로 그래프에 드래곤커브 기록할 것이다
    curve_dir = [d]
    for _ in range(gen):  # 세대 개수 만큼
        for k in range(len(curve_dir) - 1, -1, -1):  # 방향의 개수만큼, 0까지 역순으로
            # 다음 세대의 드래곤 커브는 이전 세대의 드래곤 커브의 방향에서 +1이 된다!! 
            curve_dir.append((curve_dir[k] + 1) % 4)

    # 드래곤 커브 기록하기
    for j in range(len(curve_dir)):
        # nr, nc = r + dr[curve_dir[j]], c + dc[curve_dir[j]]
        # => 이렇게하면 좌표가 누적이 안돼서 틀림..
        r += dr[curve_dir[j]]
        c += dc[curve_dir[j]]
        # if not (0 <= nr <= 100 or 0 <= nc <= 100):
        if r < 0 or r > 100 or c < 0 or c > 100:
            continue
        plane[r][c] = 1

# 2. 좌표평면에서 정사각형 찾기
answer = 0
for i in range(100):
    for j in range(100):
        if plane[i][j] == 1 and plane[i + 1][j] == 1 and plane[i][j + 1] == 1 and plane[i + 1][j + 1] == 1:
            answer += 1

print(answer)
