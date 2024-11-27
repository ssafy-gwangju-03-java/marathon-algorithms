# 1011 Fly me to the Alpha Centauri
import sys
input = sys.stdin.readline

def solve(x, y):
    cnt = 0
    distance = y - x  # 총 이동해야 할 거리

    # 최소 이동 횟수를 계산
    # 1. distance의 제곱근 구하기
    root = distance**0.5

    # 2. 제곱근을 기준으로 cnt 계산
    steps = int(root)

    # 따로 최소 cnt 안 구해도 여기서 최소 이동 횟수를 반환
    if distance == steps ** 2:  # 거리가 완전제곱수
        cnt = 2 * steps - 1
    elif distance <= steps ** 2 + steps:   # 거리가 중간범위
        cnt = 2 * steps
    else:   # 거리가 더 클 때
        cnt = 2 * steps + 1

    return cnt

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    ans = solve(x, y)
    print(ans)