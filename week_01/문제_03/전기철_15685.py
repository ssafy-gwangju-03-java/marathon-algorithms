dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
lst = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    lst[y][x] = 1
    dragon = [d]
    direction = [d]

    # 예제 1번의 방향 분석
    # 0 -> 1 -> (2,1) -> (2,3,2,1)
    # 이전의 값에 1을 더한후 reverse
    # 0 -> 1 (direction=[1] ,dragon=[0,1] )
    # 1 -> (2,1) -> (direction=[2,1] ,dragon=[0,1,2,1])
    # (2,1) ->(2,3,2,1) -> (direction=[2,3,2,1], dragon=[0,1,2,1,2,3,2,1])
    # 즉 이전 dragon에 1씩 더한 후 reverse를 했을 때 다음 세대의 direction이 된다.

    for _ in range(g + 1):
        for dir in direction:
            x += dx[dir]
            y += dy[dir]
            lst[y][x] = 1
        direction = [(i + 1) % 4 for i in dragon]
        direction.reverse()
        # print(direction)
        dragon += direction
        # print(dragon)


ans = 0
for i in range(100):
    for j in range(100):
        if lst[i][j] and lst[i + 1][j] and lst[i][j + 1] and lst[i + 1][j + 1]:
            ans += 1
print(ans)
