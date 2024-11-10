T = int(input())

for i in range(T):
    # x: 출발점, y: 도착점
    x, y = map(int, input().split())

    # 이동해야 할 총 거리 계산
    d = y - x

    # n: 한 번에 이동할 수 있는 최대 거리
    n = 0

    # 이동 거리가 n*(n+1)보다 작거나 같을 때까지 n을 증가
    # n*(n+1)은 1부터 n까지의 수를 2번씩 사용했을 때의 최대 거리
    while True:
        if d <= n * (n + 1):
            break
        n += 1

    # Case 1: 총 이동 거리가 n의 제곱보다 작거나 같을 때
    # n의 제곱은 1부터 n까지의 수를 각각 한 번씩 썼을 때의 거리
    # 이 경우 2n-1번의 이동으로 도착 가능
    if d <= n ** 2:
        print(n * 2 - 1)

    # Case 2: 총 이동 거리가 n의 제곱보다 클 때
    # 이 경우 추가 이동이 필요하므로 2n번의 이동이 필요
    else:
        print(n * 2)