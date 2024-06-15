# https://www.acmicpc.net/problem/2600

## Referenced
# https://ji-gwang.tistory.com/438
# https://geniusjo-story.tistory.com/m/660

import sys

input = sys.stdin.readline
balls = list(map(int, input().split()))


def game(k1, k2):
    """
    게임 이론
    - 첫 번째로 꺼내는 A는 자신이 이길 수 있는 경우의 수만 고름
    - 어떤 순서로 구슬을 꺼낼 통을 선택하는지는 상관 없음

    A가 항상 먼저 꺼내기에, A가 먼저 선택한 후의 모든 경로를 재귀 탐색을 통해
    DP 배열에 구슬이 담긴 두 통의 상태의 게임의 결과값을 저장

    A, B 번갈아가며 구슬을 꺼내기 때문에, 특정 플레이어의 순서를 저장하지 않고
    재귀 진입 시마다 꺼내는 플레이어의 순서가 정해짐
    """
    # 현재 통의 상태에서의 게임의 결과값이 존재한다면 결과값 반환
    if result[k1][k2] != -1:
        return result[k1][k2]

    # 첫 번째 통에서 구슬 꺼내기
    for i in range(3):
        # 구슬을 꺼낼 수 있고, 꺼낸 뒤 더 이상 구슬을 뺄 수 없다면
        if balls[i] <= k1 and not game(k1 - balls[i], k2):
            # 해당 차례의 승리
            result[k1][k2] = 1
            return 1

    # 두 번째 통에서 구슬 꺼내기
    for i in range(3):
        if balls[i] <= k2 and not game(k1, k2 - balls[i]):
            result[k1][k2] = 1
            return 1

    # 더 이상 구슬을 꺼낼 수 없다면 해당 차례의 패배
    result[k1][k2] = 0
    return 0


for _ in range(5):
    k1, k2 = map(int, input().split())

    """
    result[k1][k2]: 통에 k1, k2개의 구슬이 있을 때의 게임의 결과
    - 재귀 탐색 후의 결과가 항상 해당 순서에 뽑은 사람의 결과이므로
      game(k1, k2) 함수의 반환값은 가장 먼저 뽑는 A의 게임 결과가 됨
    - A 승리 시 1, B 승리 시 0
    """
    result = [[-1] * (k2 + 1) for _ in range(k1 + 1)]

    print("A") if game(k1, k2) else print("B")
