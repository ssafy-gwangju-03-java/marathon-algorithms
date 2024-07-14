# https://www.acmicpc.net/problem/6987

## Referenced
# https://www.acmicpc.net/board/view/124317
# https://brorica.tistory.com/206


import sys

input = sys.stdin.readline


def validator(count, win, tie, lose):
    global valid_match

    # 15번의 경기가 종료된 이후 유효한 경기 결과인지 판단
    # 모든 팀의 결과 값 합이 0이면 유효한 경기 결과
    if count == 15:
        if sum(win) == 0 and sum(tie) == 0 and sum(lose) == 0:
            valid_match = True
        return

    # 생성된 경기 목록에서 팀 선택
    team_a, team_b = matches[count]

    # 두 팀의 경기 결과는 승리 / 무승부 / 패배만 가능
    # 한 팀이 승리하면 다른 팀은 패배, 이외는 무승부
    # 가능한 모든 결과 조합을 탐색

    # 승리 / 패배가 가능할 경우
    if win[team_a] > 0 and lose[team_b] > 0:
        win[team_a] -= 1
        lose[team_b] -= 1
        validator(count + 1, win, tie, lose)
        # 재귀 종료 후 이전 값으로 복원
        win[team_a] += 1
        lose[team_b] += 1

    # 약간의 백트래킹?
    # 이미 유효한 경기 결과라는 결론이 나면 더 이상 재귀 진행 X
    if not valid_match:
        # 무승부가 가능할 경우
        if tie[team_a] > 0 and tie[team_b] > 0:
            tie[team_a] -= 1
            tie[team_b] -= 1
            validator(count + 1, win, tie, lose)
            tie[team_a] += 1
            tie[team_b] += 1

    if not valid_match:
        # 패배 / 승리가 가능할 경우
        if lose[team_a] > 0 and win[team_b] > 0:
            lose[team_a] -= 1
            win[team_b] -= 1
            validator(count + 1, win, tie, lose)
            lose[team_a] += 1
            win[team_b] += 1


# 경기 생성, 총 15번의 경기 진행
matches = []
for i in range(6):
    for j in range(i + 1, 6):
        matches.append((i, j))

results = []
for _ in range(4):
    match_result = list(map(int, input().split()))
    valid_match = False

    # 각 팀별 경기 결과 입력
    # 각 결과의 인덱스는 팀 번호
    win, tie, lose = [], [], []
    for i in range(0, 16, 3):
        win.append(match_result[i])
        tie.append(match_result[i + 1])
        lose.append(match_result[i + 2])

    validator(0, win, tie, lose)

    if valid_match:
        results.append(1)
    else:
        results.append(0)

print(*results)
