from collections import deque

N, L, R = map(int, input().split())
population = []

# 나라 초기 인구 정보 입력
for _ in range(N):
    population.append(list(map(int, input().split())))


# 하루 동안의 인구이동
def bfs(x, y, visited):
    q = deque([(x, y)])

    # 연합 국가 찾기
    total = 0   # 연합 국가 인구 합계
    uni = []    # 연합 국가 리스트
    while q:
        cur_x, cur_y = q.popleft()
        visited[cur_x][cur_y] = True
        p = population[cur_x][cur_y]
        uni.append((cur_x, cur_y))  # 연합 추가
        total += p  # 인구 추가

        for i,j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            _x, _y = cur_x + i, cur_y + j

            if (0 <= _x < N and 0 <= _y < N) :
                _p = population[_x][_y]
                if ( (L <= abs(_p - p) <= R) and (visited[_x][_y] == False)):
                    visited[_x][_y] = True
                    q.append((_x,_y))

    return uni,total, visited

day = 0
while True:
    flag = 0
    visited = [[False]*N for _ in range(N)]

    # 하루동안의 인구 이동 시작
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                uni, total, visited = bfs(i, j, visited)
                # 인구 이동
                if len(uni) > 1 :
                    flag = 1
                    for c_x, c_y in uni:
                        population[c_x][c_y] = int(total / len(uni))
    if flag == 0:
        break

    day += 1

print(day)