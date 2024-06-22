def recur(y, x):
    # 목표 지점에 도달했을 경우 경로 하나를 찾았으니까 1 반환
    if y == Y-1 and x == X-1:
        return 1
    
    # 이미 계산된 적이 있는 지점이라면, 해당 값 재사용
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0

    for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]:
        ey = y + dy
        ex = x + dx

        # 이동할 좌표가 지도 내에 있고, 현재 지점보다 낮은 지점으로만 이동
        if 0 <= ey < Y and 0 <= ex < X:
            if graph[y][x] > graph[ey][ex]:
                route += recur(ey, ex)

    # 현재 지점에서 출발하는 경로의 수를 dp 테이블에 저장
    dp[y][x] = route

    return dp[y][x]

Y, X = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
dp = [[-1 for _ in range(X)] for _ in range(Y)]
answer = recur(0, 0)

# 결과 출력
print(answer)