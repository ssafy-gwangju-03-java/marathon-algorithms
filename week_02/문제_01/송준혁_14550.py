# https://www.acmicpc.net/problem/14550

import sys

input = sys.stdin.readline


while True:
    input_str = list(map(int, input().split()))
    if len(input_str) == 1 and input_str[0] == 0:
        break

    N, S, T = map(int, input_str)
    board = [0]  # 시작점 설정
    # T번의 턴마다 각 보드 인덱스의 점수를 저장할 배열 생성
    # 최저점은 도달할 수 없는 임의의 최저 값으로 설정
    dp = [[-10000 * N] * (N + 1) for _ in range(T)]

    while len(board) != N + 1:
        board.extend(list(map(int, input().split())))

    board.append(0)  # 종료점 설정
    # T턴 내에 별을 획득했을 때의 점수를 저장
    result = set()

    # 초기값 설정
    for i in range(1, S + 1):
        dp[0][i] = board[i]

    # 직전 턴에 도달한 각 인덱스마다 1 ~ S 눈금의 주사위를 굴림
    for t in range(1, T):
        for idx in range(t, t * S + 1):
            for s in range(1, S + 1):
                # 인덱스가 보드 배열을 벗어났을 경우 무시
                if idx > N:
                    continue
                # 별에 도달했을 경우 직전 턴의 점수 저장
                if idx + s > N:
                    result.add(dp[t - 1][idx])
                # 별에 도달하지 못할 경우
                else:
                    # 현재 턴에 도달한 위치의 점수는
                    # 이전 턴의 다른 위치에서 도달했을 경우의 점수와 
                    # 현재 턴에서 도달했을 경우의 점수 중 최대값
                    dp[t][idx + s] = max(dp[t - 1][idx] + board[idx + s], dp[t][idx + s])

    print(max(result))
