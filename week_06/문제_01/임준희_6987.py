from collections import deque
import sys

def check_results(game_results):
    # 경기 진행 상황을 저장할 큐
    q = deque([(0, game_results)])
    while q:
        current_game, current_state = q.popleft()
        # 15경기가 모두 끝났을 때
        if current_game == 15:
            # 모든 점수가 0이면 리턴 1
            if all(score == 0 for score in current_state):
                return 1
            continue
        
        # 이번 경기 두 팀
        team1, team2 = games[current_game]
        # 세 가지 가능한 결과 확인 (승-패, 무-무, 패-승)
        for i in range(3):
            # 두 팀 모두 해당 결과가 가능하면
            if current_state[3*team1+i] > 0 and current_state[3*team2+2-i] > 0:
                next_state = current_state[:]
                # 경기 결과 적용
                next_state[3*team1+i] -= 1
                next_state[3*team2+2-i] -= 1
                # 다음 경기로 넘어감
                q.append((current_game+1, next_state))
    # 가능한 결과 못찾으면 리턴 0
    return 0

def world_cup():
    results = []
    for _ in range(4):
        game_results = list(map(int, sys.stdin.readline().split()))
        results.append(check_results(game_results))

    print(*results)

# 모든 가능한 경기 조합 (총 15경기)
games = [(i, j) for i in range(5) for j in range(i+1, 6)]

world_cup()